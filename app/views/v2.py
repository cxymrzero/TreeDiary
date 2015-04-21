# Created by cxy on 15/4/21 with PyCharm
# -*- coding: utf-8 -*-
from flask import Blueprint, g, request, abort
from pymongo import MongoClient
from config import config
from ..utils.util import (is_params_ok, to_json, gen_token,
                          token_required)
from ..models_v2.sns import Sns

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


@v2.route('/status/text')
def publish_text_status():
    pass