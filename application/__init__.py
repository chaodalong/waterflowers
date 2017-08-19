# -*- coding: utf-8 -*-
from flask import Flask
from .database.mysqldb import init_db


'''
设置日志handler
'''
def set_logger_handler(app):
    import logging
    from logging import Formatter
    from logging import FileHandler
    filehandler = FileHandler('/tmp/py.log', 'a+')
    filehandler.setLevel(logging.DEBUG)
    filehandler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
    app.logger.addHandler(filehandler)

'''
创建应用
'''
def create_app():
    app = Flask(__name__.split('.')[0], instance_relative_config=True)

    app.config.from_pyfile('config/sys.py')

    set_logger_handler(app)

    init_db()

    # 后台管理
    from application.controllers.admin import bp_admin
    app.register_blueprint(bp_admin, url_prefix='/admin')

    # 前端页面
    from application.controllers.front import bp_front
    app.register_blueprint(bp_front, url_prefix='/front')

    return app
