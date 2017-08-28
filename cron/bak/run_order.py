#!/usr/bin/env python
import sys, time
sys.path.append('./')

from application import create_cron_app
from application.core.redis import redis_store
from application.utils.common import md5,run_order
from woker import WorkerMaster

app = create_cron_app()
redis_key = md5(app.config.get('SECRET_KEY') + 'water_order_list:')

# muiltprocess
mworker = WorkerMaster(callback=run_order)

# set task
while True:
    task = redis_store.lpop(redis_key)
    mworker.put_task(task)


