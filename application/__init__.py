# -*- coding: utf-8 -*-
from flask import Flask
from .database.mysqldb import init_db


def set_logger_handler(app):
    """
    设置日志handler
    :param app:
    :return:
    """
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


def create_app():
    """
    创建应用
    :return: app instance
    """
    app = Flask(__name__.split('.')[0], instance_relative_config=True)

    app.config.from_pyfile('config/sys.py')

    set_logger_handler(app)

    init_db(app)

    from application.controllers.admin import bp_admin
    app.register_blueprint(bp_admin, url_prefix='/admin')

    return app
