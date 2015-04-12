# Created by cxy on 15/4/9 with PyCharm
# -*- coding: utf-8 -*-
from app import app
from ..utils.util import to_json


@app.errorhandler(404)
def handle_404(error):
    return to_json('404 not found')


@app.errorhandler(403)
def handle_403(error):
    return to_json('403 forbidden')


@app.errorhandler(405)
def handle_405(error):
    return to_json('405 method not allowed')


@app.errorhandler(500)
def handle_500(error):
    return to_json('500 internal error')


@app.errorhandler(400)
def handle_400(error):
    return to_json('400 bad request')