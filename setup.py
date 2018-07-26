from setuptools import find_packages, setup

packages = find_packages('django_upyun')

setup(
    name='django-upyun-storage',
    version=0.1,
    url='https://blog.jasonqiao36.cc/',
    author='Jason Qiao',
    author_email='jasonqiao36@gmail.com',
    description='UpYun utils for Django2.x',
    packages=packages,
    package_dir={'': 'django_upyun'},
    include_package_data=True,
    install_requires=[
        'Django>=2.0',
        'upyun==2.5.2'
    ],
    zip_safe=False,
)
