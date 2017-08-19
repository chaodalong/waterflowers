# -*-coding: utf-8-*-
from flask.blueprints import Blueprint
from .user import User
from .dashboard import Dashboard

# blue print
bp_front = Blueprint('bp_front', __package__)

# login
bp_front.add_url_rule('/login', view_func=User.as_view('login', method_name='login'))
# login
bp_front.add_url_rule('/logout', view_func=User.as_view('logout', method_name='logout'))

# dashboard
bp_front.add_url_rule('/dashbord', view_func=Dashboard.as_view('dashboard'))

__all__ = [bp_front]