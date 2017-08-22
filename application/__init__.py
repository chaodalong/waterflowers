# -*- coding: utf-8 -*-
from flask import Flask
from controllers.admin import bp_admin
from application.core.msqldb import init_db
from application.core.redis import redis_store


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


def create_web_app():
    """
    创建web应用
    :return: app instance
    """
    app = Flask(__name__.split('.')[0], instance_relative_config=True)

    app.config.from_pyfile('config/sys.py')

    set_logger_handler(app)

    init_db(app)

    redis_store.init_app(app)

    app.register_blueprint(bp_admin, url_prefix='/admin')

    return app


def create_cron_app():
    """
    创建cron应用
    :return: app instance
    """
    app = Flask(__name__.split('.')[0], instance_relative_config=True)

    app.config.from_pyfile('config/sys.py')

    set_logger_handler(app)

    init_db(app)

    redis_store.init_app(app)

    return app