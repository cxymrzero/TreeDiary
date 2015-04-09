# Created by cxy on 15/4/9 with PyCharm
# -*- coding: utf-8 -*-
class Config:
    SECRET_KEY = '\xc4\xa3\xdb\xda\x7f\x9d\x16\xf9\x02\x95\x93\xb2\x8e\x9e%\x80\xed\x10\xc8M\xda9\x96A'

class DevConfig(Config):
    MYSQL_CONN = 'mysql+mysqldb://root:jimchen@localhost:3306/tree?charset=utf8'

class ProductConfig(Config):
    MYSQL_CONN = 'mysql+mysqldb://root:Hustonline87542701:3306/tree?charset=utf8'