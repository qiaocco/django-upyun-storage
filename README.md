# Django UpYun Storage

### Django Storage for [又拍云存储](https://www.upyun.com)

## 安装

    pip install django-upyun-storage

## 配置

修改`settings.py`:

| Django Settings      | 说明                         |
| -------------------- | ---------------------------- |
| UPYUN_USERNAME       | 又拍存储服务的操作员的的姓名 |
| UPYUN_PASSWORD       | 又拍存储服务的操作员的的密码 |
| UPYUN_SERVICE        | 用于存放文件的又拍云服务名   |
| UPYUN_SERVICE_URL    | 用于访问又拍云文件的地址     |
| DEFAULT_FILE_STORAGE | 修改Django默认的文件存储类型 |

## 使用指南
用七牛托管动态生成的文件（例如用户上传的文件）

在`settings.py`里设置 `DEFAULT_FILE_STORAGE` :

    DEFAULT_FILE_STORAGE = 'django_upyun.storage.UpYunStorage'