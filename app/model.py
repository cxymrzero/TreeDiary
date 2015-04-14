# Created by cxy on 15/4/9 with PyCharm
# -*- coding: utf-8 -*-
from sqlalchemy import Column, create_engine
from sqlalchemy import String, Integer, Enum, DateTime, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
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
    open_id = Column(String(64), nullable=False)
    create_time = Column(DateTime, nullable=False)

    def __init__(self, sns_type, nickname, head_url, open_id):
        self.sns_type = sns_type
        self.nickname = nickname
        self.head_url = head_url
        self.open_id = open_id
        self.create_time = datetime.now()

    def data(self):
        return dict(sns_id=self.id, sns_type=self.sns_type,
                    sns_nickname=self.nickname, sns_head_url=self.head_url,
                    sns_create_time=self.create_time.strftime(config.TIME_FORMAT_STR)
                    )


class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    content = Column(String(500), nullable=False)
    pub_time = Column(DateTime, nullable=False)
    pic_num = Column(SmallInteger, nullable=False, default=0)

    def __init__(self, content, pic_num):
        self.content = content
        self.pub_time = datetime.now()
        self.pic_num = pic_num


class Img(Base):
    __tablename__ = 'img'
    id = Column(Integer, primary_key=True)
    img_url = Column(String(128), nullable=False)

    def __init__(self, img_url):
        self.img_url = img_url


class Model():
    def __init__(self):
        session = sessionmaker(bind=engine)
        self.session = session()

    def add_sns(self, sns_type, nickname, head_url, open_id):
        exist_sns_data = self.session.query(Sns).filter(and_(Sns.open_id == open_id, Sns.sns_type == sns_type)).first()
        if exist_sns_data:
            return exist_sns_data
        new_sns_data = Sns(sns_type, nickname, head_url, open_id)
        self.session.add(new_sns_data)
        self.session.commit()
        return new_sns_data


def init_db():
    Base.metadata.create_all(bind=engine)


def drop_db():
    Base.metadata.drop_all(bind=engine)