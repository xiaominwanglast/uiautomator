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