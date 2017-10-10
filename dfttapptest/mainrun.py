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
        testunit=unittest.TestSuite()

        #先退出账号
#        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(dologout.logout))
        #测试未登录新闻信息流页面运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_news.Nologin))
       #测试未登录视频信息流运行情况
#        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_videos.nologinvideos))


#        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login.AppTest1))
#        testunit.addTest(login.AppTest1("test_03_login_weixin"))


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



def  unitdotest(list1):
    testunit=unittest.TestSuite()

#    list1=["login_tel_news.login_news","login_tel_videos.login_videos","login_tel_discovery.login_discovery"]
    for i in list1:
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(i))



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

'''
        #测试未登录活动、精选模块运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_discovery.Nologin_discovery))
        #测试热文、红人界面运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_testhot.Hot))
        #测试未登录搜索界面运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_searchtest.search))
        #测试未登录状态下钱包、商城、我的运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_testmine.Nologin_mine))
        #测试未登录状态下收藏界面运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_testcollect.login_collect))

        #执行手机号登录
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_tel.AppTelLogin))
        #执行手机号登录后，信息流页面运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_tel_news.login_news))
        #执行手机号登录后，视频页面运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_tel_videos.login_videos))
        #执行手机号登录后，精选模块运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_tel_discovery.login_discovery))
        #执行手机号登录后，热文、红人界面运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_tel_testhot.Hot))
        #执行手机号登录后，搜索界面运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_tel_serchtest.search))
        #测试手机登录状态下钱包、商城、我的运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_testmine.login_mine))
        #测试手机登录状态下收藏运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_testcollect.login_collect))



        #执行QQ号登录
        testunit.addTest(login_other.AppLoginTest("test_01_login_QQ"))
        #执行QQ号登录后，信息流页面运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_tel_news.login_QQ_news))
        #执行QQ号登录后，视频页面运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_tel_videos.login_QQ_videos))
        #执行QQ号登录后，精选模块运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_tel_discovery.login_QQ_discovery))
        #执行QQ号登录后，热文、红人界面运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_tel_testhot.QQ_Hot))
        #执行QQ号登录后，搜索界面运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_tel_serchtest.QQ_search))
        #测试QQ号登录状态下钱包、商城、我的运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_testmine.login_mine))
        #测试QQ号登录状态下收藏运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_testcollect.login_collect))


        #执行微博登录
        testunit.addTest(login_other.AppLoginTest("test_02_login_weibo"))
        #执行微博登录后，信息流页面运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_tel_news.login_weibo_news))
        #执行微博登录后，视频页面运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_tel_videos.login_weibo_videos))
        #执行微博登录后，精选模块运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_tel_discovery.login_weibo_discovery))
        #执行微博登录后，热文、红人界面运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_tel_testhot.weibo_Hot))
        #执行微博登录后，搜索界面运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_tel_serchtest.weibo_search))
        #测试微博登录状态下钱包、商城、我的运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_testmine.login_mine))
        #测试微博登录状态下收藏运行情况
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_testcollect.login_collect))

'''
