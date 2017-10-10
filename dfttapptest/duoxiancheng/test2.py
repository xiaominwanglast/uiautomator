#coding:utf-8
import threading
import time
class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        for i in range(self.counter):
            print threading.currentThread()
            time.sleep(self.counter/2)
            print self.name+'\t'+time.ctime()
# 创建新线程
th=[]
thread1 = th.append(myThread(1, "haha", 6))
thread2 = th.append(myThread(2, "heihei", 10))

for i in th:
    i.start()
for i in th:
    i.join()
print "Exiting Main Thread"

