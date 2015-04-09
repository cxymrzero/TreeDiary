# Created by cxy on 15/4/9 with PyCharm
# -*- coding: utf-8 -*-
from sqlalchemy import Column, create_engine
from sqlalchemy import String, Integer, Enum, DateTime, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from config import config
from datetime import datetime


Base = declarative_base()  # 创建对象的基类
conn = config.MYSQL_CONN
engine = create_engine(conn)


class Sns(Base):
    __tablename__ = 'sns'
    id = Column(Integer, primary_key=True)
    sns_type = Column(Enum('1', '2', '3'), nullable=False)  # 1: weibo, 2: QQ, 3: weixin
    nickname = Column(String(64), nullable=False)
    head_url = Column(String(256), nullable=False)
    create_time = Column(DateTime, nullable=False)

    def __init__(self, sns_type, uid, nickname, head_url):
        self.sns_type = sns_type
        self.uid = uid
        self.nickname = nickname
        self.head_url = head_url
        self.create_time = datetime.strftime(config.TIME_FORMAT_STR)


class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    content = Column(String(500), nullable=False)
    pub_time = Column(DateTime, nullable=False)
    pic_num = Column(SmallInteger, nullable=False, default=0)

    def __init__(self, content, pic_num):
        self.content = content
        self.pub_time = datetime.strftime(config.TIME_FORMAT_STR)
        self.pic_num = 0


class Img(Base):
    __tablename__ = 'img'
    id = Column(Integer, primary_key=True)
    img_url = Column(String(128), nullable=False)

    def __init__(self, img_url):
        self.img_url = img_url


def init_db():
    Base.metadata.create_all(bind=engine)


def drop_db():
    Base.metadata.drop_all(bind=engine)