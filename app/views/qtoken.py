# Created by cxy on 15/4/15 with PyCharm
# -*- coding: utf-8 -*-
from qiniu import Auth
from flask import request, Blueprint, abort
from ..utils.util import to_json
from werkzeug.utils import secure_filename
from ..utils.util import is_file_a_pic

access_key = '-Ho6-iKbkpJtMmhHi0q-DsvOgEH_ktLv2BUpDeXi'
secret_key = 'fJF0skN1L6ZKholdidlrjkgHDV4B71ibmwdKXeJV'
q = Auth(access_key, secret_key)

qtoken = Blueprint('qtoken', __name__)


@qtoken.route('/')
def get_qiniu_token():
    file_name = request.args.get('file_name')
    if not file_name:
        abort(400)

    if not is_file_a_pic(file_name):
        return to_json('File to upload is not a pic!')

    file_name = secure_filename(file_name)

    bucket = 'treediary'
    token = q.upload_token(bucket, file_name)
    data = dict(qtoken=token)
    return to_json(data, success=True)