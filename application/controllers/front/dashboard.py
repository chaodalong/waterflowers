# -*-coding: utf-8 -*-
from flask import render_template, redirect, url_for, session
from flask.views import View

class Dashboard(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if 'username' in session:
            username = session['username']
            data = {'username': username}
            return render_template('dashboard/index.html', data=data)
        else:
            return redirect(url_for('bp_front.login'))