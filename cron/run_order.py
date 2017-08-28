#!/usr/bin/env python
import sys, time
sys.path.append('./')

from application import create_cron_app
from application.core.redis import redis_store
from application.utils.common import md5,run_order
import multiprocessing

app = create_cron_app()
redis_key = md5(app.config.get('SECRET_KEY') + 'water_order_list:')


def runtask(task_queue, callback):
    while True:
        task = task_queue.get()
        if task:
            print task
            callback(task)

# quque
manager = multiprocessing.Manager()
task_queue = manager.JoinableQueue()

# pool
pool = multiprocessing.Pool(processes=4)
pool.apply_async(runtask, args=(task_queue, run_order, ))

# set task
while True:
    task = redis_store.lpop(redis_key)
    task_queue.put(task)


