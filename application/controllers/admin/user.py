# -*-coding: utf-8 -*-
from flask import (render_template, request, redirect, url_for,
session, flash)
from .baseview import BaseView
from application.models.UserModel import UserModel
from application.utils.common import md5

class User(BaseView):
    methods = ['GET', 'POST']

    def __init__(self, method_name=None):
        self.method_name = method_name

    def dispatch_request(self):
        return getattr(self, self.method_name)()

    def login(self):
        self.page_title = u'登录'
        if request.method == 'POST':
            username = request.form['username']
            password = md5(request.form['password'])
            if 'username' in session:
                return redirect(url_for('bp_admin.water_index'))
            else:
                user = UserModel.query.filter(UserModel.name == username).first()
                if user is not None and user.password == password:
                    session['username'] = username
                    return redirect(url_for('bp_admin.water_index'))
                else:
                    flash(u"用户名或密码错误")
            return render_template('user/login.html', page_title=self.page_title)
        else:
            if 'username' in session:
                return redirect(url_for('bp_admin.water_index'))
            else:
                return render_template('user/login.html', page_title=self.page_title)

    def logout(self):
        self.page_title = '登出'

        if 'username' in session:
            del session['username']
        return redirect(url_for('bp_admin.login'))