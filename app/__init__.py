# Created by cxy on 15/4/9 with PyCharm
# -*- coding: utf-8 -*-
from flask import Flask
from config import config
from .views.v1 import v1


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(v1, url_prefix='/api/v1')
    return app

app = create_app()