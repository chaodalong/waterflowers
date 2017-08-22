# -*-coding: utf-8-*-
from flask.blueprints import Blueprint
from .user import User
from .water import Water

# blue print
bp_admin = Blueprint('bp_admin', __package__)

# login
bp_admin.add_url_rule('/login', view_func=User.as_view('login', method_name='login'))
# login
bp_admin.add_url_rule('/logout', view_func=User.as_view('logout', method_name='logout'))

# dashboard
bp_admin.add_url_rule('/water/index', view_func=Water.as_view('water_index', method_name='index'))
bp_admin.add_url_rule('/water/run', view_func=Water.as_view('water_run', method_name='run'))
bp_admin.add_url_rule('/water/stop', view_func=Water.as_view('water_stop', method_name='stop'))
