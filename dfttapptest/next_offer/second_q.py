#coding:utf-8
#多进程
import time
import multiprocessing
def run(data):
    print time.ctime(time.time())
    print data
if __name__=='__main__':
    p1=multiprocessing.Process(target=run,args=('11',))
    p2=multiprocessing.Process(target=run,args=('22',))
    p1.start()
    p2.start()
#-----------------------------------------------------------------------
#单进程类
#coding:utf-8
import multiprocessing,time
class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval
    def run(self):
        n = 5
        while n > 0:
            print("the time is {0}".format(time.ctime()))
            time.sleep(self.interval)
            n -= 1
if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()
#-----------------------------------------------------------------------
#多进程方法
#coding:utf-8
import multiprocessing
import time
def func(msg):
    print "msg:", msg
    time.sleep(3)
    print "end"
if __name__ == "__main__":
    pool = multiprocessing.Pool(processes = 5)
    for i in xrange(12):
        msg = "hello %d" %i
        pool.apply_async(func, (msg, ))   #维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
    pool.close()
    pool.join()
    '''
    pool.map_async(func,range(0,12))
    pool.close()
    pool.join()
    '''
#-----------------------------------------------------------------------
#多进程类
import requests
import os,time
from multiprocessing import Process,JoinableQueue
class ThreadUrl(Process):
    def __init__(self, queue):
        super(ThreadUrl, self).__init__()
        self.queue = queue
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",
        }
        self.workpath='E:\\os\\baisi_mp4'
    def run(self):
        while not self.queue.empty():
            url_name = self.queue.get()
            print u'正在下载%s'%url_name
            name=os.path.basename(url_name)
            with open(self.workpath+'\\'+name,'wb') as ps:
                ps.write(requests.get(url_name,headers=self.headers).content)
            self.queue.task_done()
def main():
#    work_List=list()
    queue=JoinableQueue()
    q=[]#url的list
    for i in q:
        queue.put(i)
    for i in range(10):
        t=ThreadUrl(queue)
        t.start()
    queue.join()
if __name__=='__main__':
    start = time.time()
    main()
    print("spend Time: %s" % (time.time() - start))
