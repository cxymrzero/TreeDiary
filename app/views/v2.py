# Created by cxy on 15/4/21 with PyCharm
# -*- coding: utf-8 -*-
from flask import Blueprint, g, request, abort
from pymongo import MongoClient
from config import config
from ..utils.util import (is_params_ok, to_json, gen_token,
                          token_required)
from ..models_v2.model import Sns, Status

v2 = Blueprint('v2', __name__)


@v2.before_request
def before_request():
    if not getattr(g, "connection", None):
        print 'connecting mongodb'
        g.connection = MongoClient()
        g.db = g.connection[config.MONGODB]


@v2.teardown_request
def teardown_request(func):
    if getattr(g, "connection", None):
        print 'closing mongodb'
        g.connection.close()


@v2.route('/')
def hello():
    return 'hello, this is version2 of TreeDiary'


@v2.route('/snsLogin/', methods=['POST'])
def sns_login():
    """
    接入第三方登录，包括微博、QQ和微信，成功则返回token
    """
    sns_type = request.form.get('sns_type')
    nickname = request.form.get('nickname')
    head_url = request.form.get('head_url')
    open_id = request.form.get('open_id')
    if not is_params_ok(sns_type, nickname, head_url, open_id):
        abort(400)

    sns_model = Sns(g.db)
    sns_id = sns_model.add_sns_info(sns_type, nickname, head_url, open_id)
    sns_id = str(sns_id)
    token = gen_token(sns_id)
    data = dict(token=token)
    return to_json(data, True)


@v2.route('/status/', methods=['POST'])
@token_required
def publish_status(user_id):
    status_type = request.form.get('status_type')
    text = request.form.get('text')
    pic_url_str = request.form.get('pic_url_str')
    has_pic = request.form.get('has_pic')
    pic_num = request.form.get('pic_num')
    if not is_params_ok(status_type, text, pic_url_str,
                        has_pic, pic_num):
        abort(400)

    status_type = str(status_type)
    has_pic = str(has_pic)
    if status_type not in ('1', '2', '3'):  # 1: blue 2: yellow 3: green
        return to_json('status type code error')
    if has_pic not in ('1', '0'):
        return to_json('has pic code error')
    if len(text) > 500:
        return to_json('status text too long')

    status_model = Status(g.db)
    # 纯文字状态
    if has_pic == '0':
        if str(pic_num) != '0':
            return to_json('pic num error')
        status_id = status_model.add_text_status(text, status_type)
        status_id = str(status_id)
        res = {'status_id': status_id}
        return to_json(res, success=True)

    if has_pic == '1':
        # 使用']'分割url
        pic_url_str = pic_url_str.strip(']')
        pic_url_list = pic_url_str.split(']')
        if len(pic_url_list) != int(pic_num):
            return to_json('pic num error')
        status_id = status_model.add_pic_status(text, status_type, pic_url_list, pic_num)
        status_id = str(status_id)
        res = {'status_id': status_id}
        return to_json(res, success=True)