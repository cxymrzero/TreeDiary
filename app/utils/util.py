# Created by cxy on 15/4/9 with PyCharm
# -*- coding: utf-8 -*-
from flask import jsonify, request
from config import config
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature
from functools import wraps


def to_json(data, success=False):
    if success:
        return jsonify({'data': {'msg': data}, 'status': 'ok'})
    return jsonify({'msg': data, 'status': 'fail'})


def gen_token(uid, expiration=31*24*60*60):
    s = Serializer(config.SECRET_KEY, expires_in=expiration)
    return s.dumps({'id': uid})


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.form.get('token')
        s = Serializer(config.SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return to_json('expired token')
        except BadSignature:
            return to_json('useless token')
        kwargs['user_id'] = data.id
        return func(*args, **kwargs)
    return wrapper