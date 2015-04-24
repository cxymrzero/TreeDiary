# Created by cxy on 15/4/23 with PyCharm
# -*- coding: utf-8 -*-
from datetime import datetime


class Sns:
    def __init__(self, db):
        self.collection = db.sns

    def add_sns_info(self, sns_type, nickname, head_url, open_id, uid):
        # 查看是否使用SNS登录过
        selector = dict(sns_type=sns_type, open_id=open_id)
        old_record = self.collection.find_one(selector)
        if old_record:
            return old_record['_id']

        data = dict(sns_type=sns_type, nickname=nickname, head_url=head_url,
                    open_id=open_id, uid=uid)
        data['sns_create_time'] = datetime.now()
        return self.collection.insert(data)


class Status:
    def __init__(self, db):
        self.c = db.status

    def add_text_status(self, text, status_type, uid):
        # 发布纯文字状态
        text_status = dict(
            text=text,
            pub_time=datetime.now(),
            pic_urls=[],
            pic_num=0,
            status_type=status_type,
            has_pic=0,
            uid=uid,
        )
        return self.c.insert(text_status)

    def add_pic_status(self, text, status_type, pic_url_list, pic_num, uid):
        # 发布含图片状态
        pic_status = dict(
            text=text,
            pub_time=datetime.now(),
            pic_urls=pic_url_list,
            pic_num=pic_num,
            status_type=status_type,
            has_pic=1,
            uid=uid,
        )
        return self.c.insert(pic_status)


class User:
    def __init__(self, db):
        self.c = db.user

    def create_user(self):
        user_info = dict(
            email=None,
            pwd=None,
            yellow=0,
            green=0,
            blue=0,
            level=0,
            create_time=datetime.now(),
        )
        return self.c.insert(user_info)

    def update_user_info(self, uid, **kwargs):
        keys = ('yellow', 'green', 'blue', 'level')
        data_to_update = {}

        u = self.c.find({'_id': uid})
        if not u:
            return None  # 用户不存在

        for key in kwargs:
            if key not in keys:
                return None  # 要修改的参数错误
            if kwargs[key] is not None:
                data_to_update.update({key: int(kwargs[key])})
        print data_to_update
        return self.c.update({'_id': uid}, {'$set': data_to_update})