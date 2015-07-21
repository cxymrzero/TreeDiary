# Created by cxy on 15/4/9 with PyCharm
# -*- coding: utf-8 -*-
from os import environ


class Config:
    SECRET_KEY = 
    TIME_FORMAT_STR = '%Y-%m-%d %H:%M:%S'
    MONGODB = 'tree'

class DevConfig(Config):
    MYSQL_CONN = 'mysql+mysqldb://root:password@localhost:3306/tree?charset=utf8'

class ProductConfig(Config):
    MYSQL_CONN = 'mysql+mysqldb://root:password@localhost:3306/tree?charset=utf8'

# 通过环境变量$USER判断是否为生产环境
user = environ.get('USER')
config = DevConfig() if user == 'mrzero' else ProductConfig()
