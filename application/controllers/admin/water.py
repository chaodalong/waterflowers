# -*-coding: utf-8 -*-
from flask import render_template, redirect, url_for, session
from .baseview import BaseView
from application.utils.common import run_order
from application.models.WaterLogModel import WaterLogModel
import time

class Water(BaseView):
    methods = ['GET', 'POST']
    page_title = u'浇花'

    def __init__(self, method_name=None):
        self.method_name = method_name

    def dispatch_request(self):
        return getattr(self, self.method_name)()

    def index(self):
        if 'username' in session:
            username = session['username']
            data = {'username': username}

            # water log
            water_logs = WaterLogModel.query.order_by(WaterLogModel.id.desc()).limit(100).all()
            return render_template('water/index.html', data=data, page_title=self.page_title, water_logs=water_logs)
        else:
            return redirect(url_for('bp_admin.login'))

    def run(self):
        run_order('begin_water')

        # 10秒后自动关闭，防止水溢出
        time.sleep(10)
        run_order('auto_stop_water')

        return redirect(url_for('bp_admin.water_index'))

    '''
    停止浇花
    '''
    def stop(self):
        run_order('stop_water')
        return redirect(url_for('bp_admin.water_index'))