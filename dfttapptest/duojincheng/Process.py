#coding:utf-8

#process
#创建函数并将其作为单个进程
import multiprocessing
import time

def worker_1(interval):
    print "worker_1"
    time.sleep(interval)
    print "end worker_1"

def worker_2(interval):
    print "worker_2"
    time.sleep(interval)
    print "end worker_2"

def worker_3(interval):
    print "worker_3"
    time.sleep(interval)
    print "end worker_3"

if __name__ == "__main__":
    p1 = multiprocessing.Process(target = worker_1, args = (1,))
    p2 = multiprocessing.Process(target = worker_2, args = (3,))
    p3 = multiprocessing.Process(target = worker_3, args = (10,))

    p1.start()
    p2.start()
    p3.start()

    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    print "END!!!!!!!!!!!!!!!!!"
'''
import multiprocessing
import time
def worker(interval):
    n = 5
    while n > 0:
        print("The time is {0}".format(time.ctime()))
        time.sleep(interval)
        n -= 1

if __name__ == "__main__":
    p = multiprocessing.Process(target = worker, args = (3,))
    p.start()
    print "p.pid:", p.pid
    print "p.name:", p.name
    print "p.is_alive:", p.is_alive()
'''