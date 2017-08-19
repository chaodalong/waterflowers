# -*-coding: utf-8 -*-
from flask import (render_template, request, redirect, url_for,
session, flash)
from flask.views import View
from application.models.UserModel import UserModel
from application.utils.common import md5

class User(View):
    methods = ['GET', 'POST']

    def __init__(self, method_name=None):
        self.method_name = method_name

    def dispatch_request(self):
        return getattr(self, self.method_name)()

    def login(self):
        if request.method == 'POST':
            username = request.form['username']
            password = md5(request.form['password'])

            if 'username' in session:
                return redirect(url_for('bp_front.dashboard'))
            else:
                user = UserModel.query.filter(UserModel.name == username).first()
                if user is not None and user.password == password:
                    session['username'] = username
                    return redirect(url_for('bp_front.dashboard'))
                else:
                    flash(u"用户名或密码错误")
            return render_template('user/login.html')
        else:
            return render_template('user/login.html')

    def logout(self):
        if 'username' in session:
            del session['username']
        return redirect(url_for('bp_front.login'))