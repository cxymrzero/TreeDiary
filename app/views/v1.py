# Created by cxy on 15/4/9 with PyCharm
# -*- coding: utf-8 -*-
from flask import Blueprint, request


v1 = Blueprint('v1', __name__)


@v1.route('/')
def index():
    return 'hello'