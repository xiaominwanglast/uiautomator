#coding:utf-8
import time
import threading
def foo(number):
    return number
def gg(number,count):
    return number*count
class MyThread(threading.Thread):
    def __init__(self, number,count):
        threading.Thread.__init__(self)
        self.number = number
        self.count=count
    def run(self):
        if self.count=='s':
            time.sleep(self.number)
            print time.ctime()
            self.result = foo(self.number)
        elif self.count=='d':
            time.sleep(self.number)
            print time.ctime()
            self.result=gg(self.number,self.count)
    def get_result(self):
        return self.result

th=[]
th.append(MyThread(3,'s'))
th.append(MyThread(5,'d'))
for i in th:
    i.setDaemon(True)
    i.start()
i.join()
print th[0].get_result()
print th[1].get_result()
