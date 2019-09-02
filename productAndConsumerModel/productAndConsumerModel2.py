#!/usr/bin/python
# -*- coding:utf-8 -*-

import threading, time , queue

q = queue.Queue()

def Produce(name):
    count = 0
    while count < 10:
        print("厨师%s在做包子中....."%name)
        time.sleep(2)
        q.put(count)
        print("product%s已经做好了第%s个包子"%(name, count))
        count += 1
        q.join()
        print('ok....')

def Consumer(name):
    count = 0
    while count < 10:
        time.sleep(2)
        data = q.get()
        print("%seating..."%name)
        time.sleep(4)
        q.task_done()
        print("\033[32;1mConsumer %s已经把第%s个包子吃了...\033[0m'"%(name,data))
        count += 1


if __name__ == "__main__":
    p1 = threading.Thread(target=Produce,args=("A",))
    c1 = threading.Thread(target=Consumer,args=("B",))
    c2 = threading.Thread(target=Consumer,args=("C",))
    c3 = threading.Thread(target=Consumer,args=("D",))
    p1.start()
    c1.start()
    c2.start()
    c3.start()


