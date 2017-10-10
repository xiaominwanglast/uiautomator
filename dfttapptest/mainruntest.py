#-*- coding: UTF-8 -*-


import  unittest
import  HTMLTestRunner
import dologout
import nologin_discovery
import nologin_news
import nologin_videos
import nologin_testhot
import nologin_testmine
import nologin_testcollect

import time
import nologin_searchtest

import login_tel
import login_tel_news
import login_tel_videos
import login_tel_discovery
import login_tel_testhot
import login_tel_serchtest
import login_other
import login_testmine
import login_testcollect


import logging

logging.basicConfig()


'''
头条快报
appPackage=com.yicen.ttkb
appActivity=com.oa.eastfirst.activity.WelcomeActivity

东方头条
appPackage=com.songheng.eastnews
appActivity=com.oa.eastfirst.activity.WelcomeActivity
'''

'''
subprocess.Popen("appium.cmd")

time.sleep(20)
'''

def do_testunit():
    while True:
        #执行未登录账号页面监控
        lista=[nologin_news.Nologin,nologin_videos.nologinvideos,nologin_discovery.Nologin_discovery,nologin_testhot.Hot,nologin_searchtest.search,nologin_testmine.Nologin_mine,
               nologin_testcollect.login_collect]


        #执行手机号登录账号页面监控
        listb=[login_tel.AppTelLogin,login_tel_news.login_news,login_tel_videos.login_videos,login_tel_discovery.login_discovery,
               login_tel_testhot.Hot,login_tel_serchtest.search,login_testmine.login_mine,login_testcollect.login_collect]


        #执行QQ登录账号页面监控
        listc=[login_tel_news.login_QQ_news,login_tel_videos.login_QQ_videos,login_tel_discovery.login_QQ_discovery,
               login_tel_testhot.QQ_Hot,login_tel_serchtest.QQ_search,login_testmine.login_mine,login_testcollect.login_collect]

        #执行微博登录账号页面监控
        listd=[login_tel_news.login_weibo_news,login_tel_videos.login_weibo_videos,login_tel_discovery.login_weibo_discovery,
               login_tel_testhot.weibo_Hot,login_tel_serchtest.weibo_search,login_testmine.login_mine,login_testcollect.login_collect]

        testunit=unitdotest(lista,listb,listc,listd)



        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        print now
#定义个报告存放路径，支持相对路径
        filename = 'D:/test_result/'+now+"-result.html"
#    filename = now + "_result.html"
        fp = file(filename, 'wb')
        print ('打开文件'.decode("utf-8"))
#定义测试报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行情况：')
#运行测试用例
        runner.run(testunit)
        fp.close()  #关闭报告文件


def  unitdotest(list1,list2,list3,list4):
    testunit=unittest.TestSuite()

#    list1=[login_tel_news.login_news,login_tel_videos.login_videos,login_tel_discovery.login_discovery]
    #加载未登录测试类
    for i in list1:
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(i))

    #加载登录手机号的测试类
    for i in list2:
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(i))

    #QQ号登录
  #  testunit.addTest(login_other.AppLoginTest("test_01_login_QQ"))

    #加载登录QQ后的测试类
#    for i in list3:
#        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(i))

    #微博登录
    testunit.addTest(login_other.AppLoginTest("test_02_login_weibo"))

    #加载登录微博后的测试类
 #   for i in list4:
 #       testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(i))

    return testunit


if __name__== "__main__":
    do_testunit()



'''
    scheduler = BlockingScheduler()
    scheduler.add_job(do_testunit,'cron', minute='23', hour='16')
    print('Press Ctrl+C to exit')
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
'''


