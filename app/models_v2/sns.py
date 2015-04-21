# Created by cxy on 15/4/21 with PyCharm
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