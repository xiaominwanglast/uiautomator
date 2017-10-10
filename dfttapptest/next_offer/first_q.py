#coding:utf-8
#多线程
#coding:utf-8
import threading
import time
def run(data1,data2):
    print time.strftime('%H:%M:%S',time.localtime(time.time()))
    print threading.currentThread()
    print data1,data2
thread1=threading.Thread(target=run,name='thread1',args=('11','22',))
thread2=threading.Thread(target=run,name='thread2',args=('33','44',))
thread1.start()
thread2.start()
#----------------------------------------------------------------------
#多线程类
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
  #  i.setDeamo(True)
    i.start()
print "Exiting Main Thread"
#-----------------------------------------------------------------------
#线程池
#coding:utf-8
import requests
import threading
from requests.exceptions import ConnectTimeout,HTTPError
import time
import Queue
class ThreadUrl(threading.Thread):
    def __init__(self, queue,Ttype,data):
        threading.Thread.__init__(self)
        self.queue = queue
        self.type=Ttype
        self.data=data
        self.session=requests.Session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",
        }
        self.workpath='E:\\os\\baisi_mp4'
    def run(self):
        if self.type=='post':
            while not self.queue.empty():
                url_name = self.queue.get()
                try:
                    start_time=time.time()
                    rq=self.session.post(url=url_name,data=self.data,timeout=5)
                    end_time=time.time()
                    print end_time-start_time
                except HTTPError as e:
                    print e
                except ConnectTimeout as e:
                    print e
                self.queue.task_done()
def main(Turl,Ttype,data):
    queue=Queue.Queue()
    p=[Turl]*16
    for i in p:
        queue.put(i)
    for t in range(4):
        t=ThreadUrl(queue,Ttype,data)
        t.setDaemon(True)
        t.start()
    queue.join()
if __name__=='__main__':
    start = time.time()
    url='https://minisearch.dftoutiao.com/hotwords/hot'
    main(url,'post',{"type":'now'})