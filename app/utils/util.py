# Created by cxy on 15/4/9 with PyCharm
# -*- coding: utf-8 -*-
from flask import jsonify
from config import config
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature


def to_json(data, success=False):
    if success:
        return jsonify({'data': data, 'status': 'ok'})
    return jsonify({'msg': data, 'status': 'fail'})


def gen_token(uid, expiration=31*24*60*60):
    s = Serializer(config.SECRET_KEY, expires_in=expiration)
    return s.dumps({'id': uid})