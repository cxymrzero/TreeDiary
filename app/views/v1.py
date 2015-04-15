# Created by cxy on 15/4/9 with PyCharm
# -*- coding: utf-8 -*-
from flask import Blueprint, request, abort
from ..model import Model, Img
from ..utils.util import to_json, gen_token, token_required, is_params_ok


v1 = Blueprint('v1', __name__)


@v1.route('/')
def index():
    return 'hello'


@v1.route('/snsLogin/', methods=['POST'])
def get_data_from_sns():
    """
    接入第三方登录，包括微博、QQ和微信，若创建成功则返回用户登录token
    """
    sns_type = request.form.get('sns_type')
    nickname = request.form.get('nickname')
    head_url = request.form.get('head_url')
    open_id = request.form.get('open_id')
    if not is_params_ok(sns_type, nickname, head_url, open_id):
        abort(400)

    model = Model()
    new_sns_data = model.add_sns(sns_type, nickname, head_url, open_id)

    if new_sns_data:
        data = new_sns_data.data()
        token = gen_token(new_sns_data.id)
        data.update(token=token)
        return to_json(data, success=True)
    else:
        return to_json('sns login error')


@v1.route('/status/text/', methods=['POST'])
@token_required
def publish_text_status(user_id):
    content = request.form.get('content')
    status_type = request.form.get('status_type')
    if not is_params_ok(content, status_type):
        abort(400)

    model = Model()
    new_status = model.add_text_status(content, status_type)
    if new_status:
        data = {'status_id': new_status.id}
        return to_json(data, success=True)
    return to_json('oops, an error occurred')


@v1.route('/status/mix/', methods=['POST'])
@token_required
def publish_status(user_id):
    pic_num = request.form.get('pic_num')
    content = request.form.get('content')
    pic_urls = request.form.get('pic_urls')
    status_type = request.form.get('status_type')
    if not is_params_ok(pic_num, content, pic_urls, status_type):
        abort(400)
    pic_num = int(pic_num)

    # 使用']'分割url
    pic_urls = pic_urls.strip(']')
    pic_url_list = pic_urls.split(']')
    if len(pic_url_list) != pic_num:
        print pic_url_list
        return to_json('pic url error')

    model = Model()
    pic_ids = []
    for pic_url in pic_url_list:
        img = Img(pic_url)
        model.session.add(img)
        model.session.commit()
        pic_ids.append(img.id)

    pic_id_str = ','.join(map(str, pic_ids))
    status = model.add_mix_status(content, pic_num, pic_id_str, status_type)
    data = dict(status_id=status.id)
    return to_json(data, success=True)