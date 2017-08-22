# -*-coding: utf-8 -*-
from flask import render_template, redirect, url_for, session
from application.core.baseview import BaseView
from application.core.redis import redis_store
from application.models.WaterLogModel import WaterLogModel
from application.utils.common import md5
import flask


class Water(BaseView):
    """
    浇花控制器类
    """
    methods = ['GET', 'POST']
    page_title = u'浇花'

    def __init__(self, method_name=None):
        self.method_name = method_name
        self.order_redis_key = md5(flask.current_app.config.get('SECRET_KEY') + 'water_order_list:')

    def dispatch_request(self):
        return getattr(self, self.method_name)()

    def index(self):
        """
        浇花首页
        :return:
        """
        if 'username' in session:
            username = session['username']
            data = {'username': username}

            # water log
            water_logs = WaterLogModel.query.order_by(WaterLogModel.id.desc()).limit(100).all()
            return render_template('water/index.html', data=data, page_title=self.page_title, water_logs=water_logs)
        else:
            return redirect(url_for('bp_admin.login'))

    def run(self):
        """
        开始浇花
        :return:
        """
        redis_store.rpush(self.order_redis_key, 'begin_water')
        return redirect(url_for('bp_admin.water_index'))


    def stop(self):
        """
        停止浇花
        :return:
        """
        redis_store.rpush(self.order_redis_key, 'stop_water')
        return redirect(url_for('bp_admin.water_index'))