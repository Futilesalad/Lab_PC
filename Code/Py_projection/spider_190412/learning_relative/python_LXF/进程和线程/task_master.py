#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'F_tile_chen'
__mtime__ = ''
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
# task_master
import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()

# 接受结果的队列
result_queue = queue.Queue()


def re_task_queue():
    global task_queue
    return task_queue


# 自定义函数re_result_queue

def re_result_queue():
    global result_queue
    return result_queue


# 从basemanager继承queueManager
class QueueManager(BaseManager):
    pass


if __name__ == '__main__':
    # 把两个Queue都注册到网上， callable参数关联了Queue对象
    QueueManager.register('get_task_queue', callable=re_task_queue)
    QueueManager.register('get_result_queue', callable=re_result_queue)

    # 绑定端口 5000 设置验证码 'abc'
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

    # 启动Queue

    manager.start()

    # 获取通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放入任务

    for i in range(10):
        n = random.randint(0, 1000)
        print('Put tast %d...' % n)
        task.put(n)

    # 从result队列 读取结果

    print('Trying to get results......')
    for i in range(10):
        # r = result.get(True, timeout=10)
        r = result.get(True)
        print("Result: %s" % r)

    # 关闭
    manager.shutdown()
    print("master exit...")
