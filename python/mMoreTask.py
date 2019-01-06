#coding=utf-8

import threading
import time

# 多线程任务
class mMoreTask:
    def __init__(self):
        self.thread_list = []

    def addTask(self, fuc_name, args):
        t = threading.Thread(target=fuc_name, args=args)
        self.thread_list.append(t)
        pass

    def run(self):
        for x in self.thread_list:
            self.thread_list[x].start()

        for x in self.thread_list:
            self.thread_list[x].join()
        pass

def tt1(nnn):
    print(nnn + ", time111:%s" % time.time())

def tt2(nnn):
    print(nnn + ", time222:%s" % time.time())

T = m2MoreTask()
T.addTask(tt1, "aaa")
T.addTask(tt2, "bbb")
T.run()