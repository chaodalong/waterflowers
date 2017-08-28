# -*-coding: utf-8 -*-
import multiprocessing
import os, time


class WorkerMaster(object):
    """
    master class
    1、fork process work
    2、bind callback fuc
    3、write task into queue
    """
    # master process pid
    master_pid = ''

    # worker process nums
    __worker_nums = 4

    # worker process dict
    __worker_list = dict()

    # callback function
    __callback = ''

    def __init__(self, worker_nums=None, callback=None):
        if worker_nums is not None:
            self.__worker_nums = worker_nums

        self.master_pid = os.getpid()
        self.queue = multiprocessing.JoinableQueue()
        self.__callback = callback

        # create worker
        self.__create_worker()

    def __create_worker(self):
        """
        fork children process
        :return:
        """
        for i in xrange(self.__worker_nums):
            self.__fork_worker()

    def __fork_worker(self):
        worker = Worker(self.queue)
        worker.set_callback(self.__callback)
        worker.start()
        self.__worker_list[worker.pid] = worker

    def __check_worker(self):
        """
        check worker status, refork
        :return:
        """
        for k in self.__worker_list.keys():
            w = self.__worker_list[k]
            if not w.is_alive():
                # del worker
                del self.__worker_list[k]

                # fork new worker
                self.__fork_worker()

    def put_task(self, task):
        """
        write task into queue
        :param task:
        :return:
        """
        result = False
        if task:
            # check worker process
            self.__check_worker()

            # put task
            result = self.queue.put(task)
        return result


class Worker(multiprocessing.Process):
    """
    task worker
    get task from queue && run
    """
    # time expire second
    __p_expire = 5

    __callback = ''

    def __init__(self, task_queue):
        multiprocessing.Process.__init__(self)
        self.queue = task_queue
        self.__live_begin = int(time.time())

    def run(self):
        """
        run target funtion
        :return:
        """
        while True:
            try:
                task = self.queue.get(block=True, timeout=1)
            except:
                task = None
                pass

            # run task
            if task is not None:
                # print self.pid, task, self.__callback
                self.__callback(task)
                self.queue.task_done()

            # live check
            if int(time.time()) - self.__live_begin >= self.__p_expire:
                exit(0)

            time.sleep(1)

    def set_callback(self, callback):
        """
        set callback function
        :param callback:
        :return:
        """
        self.__callback = callback

