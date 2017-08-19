# -*-coding: utf-8 -*-
from flask import render_template, redirect, url_for, session
from .baseview import BaseView

class Water(BaseView):
    methods = ['GET', 'POST']
    page_title = u'浇花'

    def dispatch_request(self):
        if 'username' in session:
            username = session['username']
            data = {'username': username}
            return render_template('water/index.html', data=data, page_title=self.page_title)
        else:
            return redirect(url_for('bp_admin.login'), page_title=self.page_title)