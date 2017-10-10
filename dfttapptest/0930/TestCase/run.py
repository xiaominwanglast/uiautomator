#coding:utf-8

from testlogin import login
import unittest
import sys
import ConfigParser
import os

import time
from apscheduler.schedulers.blocking import BlockingScheduler

import logging

logging.basicConfig()
sys.path.append (r"..")
#sys.path.append("E:\\wxm\\pycharm\\python\\dfttapptest\\0930\\PO")
from  PO import  adbUtils
from PO import judge


def readmsg():
    config = ConfigParser.ConfigParser()

    with open(os.path.dirname(os.getcwd())+"\\config\\appconfig.ini","r") as cfgfile:
        config.readfp(cfgfile)
        packname=config.get("appinstall","packname")
        installname=config.get("appinstall","installname")

    return packname,installname



def do_testunit():
    print (u"--------------------开始执行登录模块的测试用例-------------------------------")
    testunit=unittest.TestSuite()
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login))
    unittest.TextTestRunner(verbosity=2).run(testunit)
    print ("\n")



if __name__== "__main__":
    #判断是否安装了对应的app，如果安装了就打印出版本号
    print (u"-----------------判断是否安装了app，未安装进行安装，安装了打印出版本号---------------------")
    judge.testinstall(readmsg()[0],readmsg()[1])

    #判断手机网络连接是否正常
    adb=adbUtils.ADB()
    if (judge.testwifi(adb)=="network not connect"):
        print (u"----------------------------手机网络异常，请重新连接------------------------")
        sys.exit()
    else:
        print (u"网络正常")




#开启定时任务	
    config = ConfigParser.ConfigParser()
    with open(os.path.dirname(os.getcwd())+"\\config\\config.ini","r") as cfgfile:
        config.readfp(cfgfile)
        start_minute=config.get("time","start_minute")
        start_hour=config.get("time","start_hour")

    print (u"定时任务开启-------测试执行任务将从%s时%s分开始执行----------------"%(start_hour,start_minute))

    scheduler = BlockingScheduler()
    scheduler.add_job(do_testunit,'cron', minute=start_minute, hour=start_hour)
    print('Press Ctrl+C to exit')
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

