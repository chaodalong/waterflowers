# -*-coding: utf-8-*-
from flask.blueprints import Blueprint
from .user import User, UserLogin

# blue print
bp_admin = Blueprint('bp_admin', __package__)

# user api
bp_admin.add_url_rule('/user/', view_func=User.as_view('text'))

# login
bp_admin.add_url_rule('/login/', view_func=UserLogin.as_view('login'))

__all__ = [bp_admin]