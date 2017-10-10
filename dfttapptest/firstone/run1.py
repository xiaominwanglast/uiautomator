import os,time
from apscheduler.schedulers.blocking import BlockingScheduler
def run():
    print 'now_time is:%s'%time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    os.system('cd E:\\wxm\\pycharm\\python\\dfttapptest\\firstone & scrapy crawl baidunews')

if __name__=='__main__':
    print 'now_time is:%s'%time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    scheduler=BlockingScheduler()
    scheduler.add_job(run,'interval',minutes=10)
    scheduler.start()