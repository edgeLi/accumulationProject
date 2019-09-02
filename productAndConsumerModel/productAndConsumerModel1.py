#!/usr/bin/python
# -*- coding:utf-8 -*-

import threading,time,queue

q = queue.Queue()

def Produce(name):
    count = 0
    while count < 10:
        print("厨师%s在做包子中..." % name)
        time.sleep(2)
        q.put(count)
        print("produce%s已经做好了第%s个包子"%(name,count))
        count += 1
        print("oking....")

def Consumer(name):
    count = 0
    while count < 10:
        time.sleep(2)
        if not q.empty():
            data = q.get()
            print("\033[32;1mConsumer %s 已经把第%s个包子吃了...\033[0m" %(name,data))
        else:
            print("包子被吃完了....")
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

