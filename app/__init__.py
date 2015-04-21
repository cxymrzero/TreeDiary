# Created by cxy on 15/4/9 with PyCharm
# -*- coding: utf-8 -*-
from flask import Flask
from config import config
from views.v1 import v1
from views.qtoken import qtoken
from views.v2 import v2


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(v1, url_prefix='/api/v1')
    app.register_blueprint(v2, url_prefix='/api/v2')
    app.register_blueprint(qtoken, url_prefix='/api/qtoken')
    return app

app = create_app()