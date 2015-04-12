# Created by cxy on 15/4/9 with PyCharm
# -*- coding: utf-8 -*-
from flask import Blueprint, request
from ..model import Model
from ..utils.util import to_json, gen_token


v1 = Blueprint('v1', __name__)


@v1.route('/')
def index():
    return 'hello'


@v1.route('/snsLogin', methods=['POST'])
def get_data_from_sns():
    """
    接入第三方登录，包括微博、QQ和微信，若创建成功则返回用户登录token
    """
    sns_type = request.form['sns_type']
    nickname = request.form['nickname']
    head_url = request.form['head_url']

    model = Model()
    new_sns_data = model.add_sns(sns_type, nickname, head_url)

    if new_sns_data:
        data = new_sns_data.data()
        token = gen_token(new_sns_data.id)
        data.update(token=token)
        return to_json(data, success=True)
    else:
        return to_json('sns login error')