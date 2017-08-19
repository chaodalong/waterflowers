# -*-coding: utf-8 -*-
from flask import render_template, make_response, jsonify, request, flash
from flask.views import View
from application.models.UserModel import UserModel

class User(View):
    '''
    用户类
    '''
    methods = ['GET', 'POST']

    def dispatch_request(self):
        user = UserModel.query.filter(UserModel.id == 2).first()
        user_obj = {"id":user.id, "name":user.name}
        return jsonify(user_obj)

class UserLogin(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if request.method == 'POST':
            username = request.form['username']
            user = UserModel.query.filter(UserModel.name == username).first()
            if user is None:
                _user_save = UserModel(name=username)
                UserModel.db_session.add(_user_save)
                UserModel.db_session.commit()
                flash(u"登陆失败！")
            else:
                UserModel.query.filter(UserModel.id > 2).update({UserModel.name:'tets2'})
                UserModel.db_session.commit()
                flash(u"登陆成功！")
            return render_template('user/login.html')
        else:
            return render_template('user/login.html')