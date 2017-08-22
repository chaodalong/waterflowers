# -*-coding: utf-8 -*-
from flask.views import View


class BaseView(View):
    """
    即插视图基础类（页面通用属性放在这）
    """
    page_title = ''