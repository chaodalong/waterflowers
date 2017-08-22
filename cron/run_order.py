#!/usr/bin/env python
import sys, time
sys.path.append('./')

from application import create_cron_app
from application.core.redis import redis_store
from application.utils.common import md5,run_order

app = create_cron_app()

redis_key = md5(app.config.get('SECRET_KEY') + 'water_order_list:')
while True:
    order = redis_store.lpop(redis_key)
    run_order(order)
    time.sleep(1)


