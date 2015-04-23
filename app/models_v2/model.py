# Created by cxy on 15/4/23 with PyCharm
# -*- coding: utf-8 -*-
from datetime import datetime


class Sns:
    def __init__(self, db):
        self.collection = db.sns

    def add_sns_info(self, sns_type, nickname, head_url, open_id):
        # 查看是否使用SNS登录过
        old_record = self.collection.find_one({'sns_type': sns_type, 'open_id': open_id})
        if old_record:
            return old_record['_id']

        data = dict(sns_type=sns_type, nickname=nickname, head_url=head_url,
                    open_id=open_id)
        data['sns_create_time'] = datetime.now()
        return self.collection.insert(data)


class Status:
    def __init__(self, db):
        self.c = db.status

    def add_text_status(self, text, status_type):
        # 发布纯文字状态
        text_status = dict(
            text=text,
            pub_time=datetime.now(),
            pic_urls=[],
            pic_num=0,
            status_type=status_type,
            has_pic=0,
        )
        return self.c.insert(text_status)

    def add_pic_status(self, text, status_type, pic_url_list, pic_num):
        # 发布含图片状态
        pic_status = dict(
            text=text,
            pub_time=datetime.now(),
            pic_urls=pic_url_list,
            pic_num=pic_num,
            status_type=status_type,
            has_pic=1,
        )
        return self.c.insert(pic_status)