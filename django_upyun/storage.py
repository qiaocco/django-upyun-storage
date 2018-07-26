from io import BytesIO
from urllib.parse import urljoin

from django.conf import settings
from django.core.files import File
from django.core.files.storage import Storage

import upyun
from upyun import UpYunServiceException


class UpYunStorage(Storage):
    def __init__(self, service=None, username=None, password=None, service_url=None):
        self.service = service or settings.UPYUN_SERVICE
        self.username = username or settings.UPYUN_USERNAME
        self.password = password or settings.UPYUN_PASSWORD
        self.api_url = "http://v0.api.upyun.com"
        self.service_url = service_url or settings.UPYUN_SERVICE_URL
        self.up = upyun.UpYun(service=self.service, username=self.username, password=self.password)

    def _open(self, name, mode="rb"):
        file = UpYunFile(name, self, mode)
        return file

    def _save(self, name, content):
        self.up.put(name, content)
        return name

    def _read(self, name):
        res = self.up.get(name)
        return res.encode()

    def delete(self, name):
        pass

    def _file_stat(self, name, silent=False):
        res = self.up.getinfo(name)
        if res is None and not silent:
            raise FileNotFoundError
        return res

    def exists(self, name):
        try:
            msg = self._file_stat(name)
            if msg['file-type']:
                return True
        except UpYunServiceException as e:
            if e.status == 404:
                return False
        return False

    def size(self, name):
        res = self._file_stat(name)
        return res['file-size']

    def listdir(self, path):
        if not path.endswith('/'):
            path += '/'

        res = self.up.getlist(path)
        directories, files = [], []

        for entry in res:
            if entry['type'] == 'F':
                directories.append(f"{path}{entry['name']}")
            elif entry['type'] == 'N':
                files.append(f"{path}{entry['name']}")

        return directories, files

    def url(self, name):
        return urljoin(self.service_url, name)


class UpYunFile(File):
    def __init__(self, name, storage, mode):
        self.name = name
        self._storage = storage
        self._mode = mode
        self.file = BytesIO()
        self._is_dirty = False
        self._is_read = False
