#coding:utf-8
import  unittest
import HTMLTestRunner
from apptest.TestCase import login_tel
from apscheduler.schedulers.blocking import BlockingScheduler
from apptest.Public import  write_represult
import logging
import  os
import time
from apptest.Public.email_all import smail
from apptest.Public import write_summary
from apptest.Public import readconfig
from apptest.Public import  processfile
from apptest.TestCase import  nologin_testmine
from apptest.TestCase import nologin_testnews
from apptest.TestCase import  nologin_testSearch
from apptest.TestCase import  nologin_testdiscovery
from apptest.TestCase import  nologin_testhot
from apptest.TestCase import  nologin_testVideo
from apptest.TestCase import nologin_channelUI
from apptest.TestCase import nologin_choice
from apptest.TestCase import login_testvideos
from apptest.TestCase import login_testhot
from apptest.TestCase import login_testdiscovery
from apptest.TestCase import login_testnews
from apptest.TestCase import login_testSearch
from apptest.TestCase import login_testmine_other
from apptest.TestCase import test_web
from apptest.TestCase.collect import login_testcollect
from apptest.TestCase.collect import nologin_testcollect
from apptest.TestCase import dologout
from apptest.TestCase import login_choiceUI
from apptest.TestCase.mine import history_read
from apptest.TestCase.mine import mesg_test
from apptest.TestCase.mine import offline_downloadnews
from apptest.TestCase.mine import purseUI
from apptest.TestCase.mine import invitefs_cloudopen
from apptest.TestCase.mine import task_dailyUI
from apptest.TestCase.mine import reward_feedback
from apptest.TestCase.mine import nologin_purseUI
from apptest.TestCase.mine import nologin_mall
from apptest.TestCase.mine import nologin_despoil
from apptest.TestCase.mine import nologin_inviteUI
from apptest.TestCase import login_channelUI
from apptest.TestCase.mine import login_mall
from apptest.TestCase.mine import login_despoil
from apptest.TestCase.mine import login_mesgtest
from apptest.TestCase.mine import login_taskcenter
from apptest.TestCase.mine import login_historyread
from apptest.TestCase.mine import login_offlinedown
from apptest.TestCase.mine import login_rewardback
from apptest.TestCase import login_doset
from apptest.TestCase.mine import login_mineimage
from apptest.TestCase import reset_background
from apptest.TestCase import tuisong
from apptest.TestCase import login_tuisong
logging.basicConfig()
timeflag=True
def do_testunit():
    print (u"--------------------开始执行测试用例-------------------------------")

    testunit=unittest.TestSuite()
    #检查网络
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(test_web.webstate))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_testnews.nologin_news))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_channelUI.nologin_channelUI))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_testVideo.nologin_video))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_testdiscovery.nologin_discovery))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_choice.nologin_choice))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_testhot.nologin_Hot))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_testSearch.nologin_serach))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_testmine.nologin_mine))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_testcollect.nologin_test_collect))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_purseUI.nologin_purse))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_mall.mallUI))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_despoil.despoilUI))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(mesg_test.mesg))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_inviteUI.nologin_invite))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(task_dailyUI.UItask))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(history_read.hisread))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(tuisong.Tuisong))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(offline_downloadnews.dlnews))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(reward_feedback.rewardfeedback))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(dologout.setUI))
    #做个随机登陆与随机黑白屏幕操作
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_tel.login))
    #登陆后测试
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_testnews.login_news))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_channelUI.login_channel))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_testvideos.login_videos))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_testdiscovery.login_discovery))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_choiceUI.login_choice))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_testhot.login_hot))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_testSearch.login_search))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_testmine_other.login_mine))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_mineimage.login_imageUI))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_testcollect.login_Collect))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(purseUI.purseUI))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_mall.login_mall))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_despoil.login_despoil))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_mesgtest.login_mesg))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(invitefs_cloudopen.cloudopen))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_taskcenter.login_taskcenterUI))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_historyread.login_historyreadUI))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_tuisong.login_tuisong))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_offlinedown.login_offlinedownUI))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_rewardback.login_rewardbackUI))
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(login_doset.login_setUI))
    #恢复环境，退出登陆操作
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(reset_background.reset))
    '''
    #检测appium服务器是否开启
    if not os.popen('netstat -ano|findstr 4723|findstr LISTENING').read():
        os.system("start /b appium --address 127.0.0.1 --port 4723")
        time.sleep(8)
    '''
    #统计suite的用例总数
    print (u"测试单元总数")
    print 'suite_number is '+ str(str(testunit).count('unittest.suite.TestSuite tests=')-1)

    #删除截图与结果
    print(u"删除历史记录文件")
    for i in [os.path.dirname(os.getcwd())+"\\screen",os.path.dirname(os.getcwd())+"\\result"]:
        readconfig.removeall(i)
    '''
    #修改配置文件
    print (u"修改配置文件")
    txt=os.popen("adb shell dumpsys package com.songheng.eastnews |findstr versionName").read()
    data=txt.strip().split('=')[1]
    print readconfig.setappVersion(data)
    '''
    #开始时间
    time_start=time.time()
    print time_start

    #打印此时开始时间
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    print now

    #定义个报告存放路径，支持相对路径
    filename =os.path.dirname(os.getcwd())+ '\\result\\'+now+"-result.html"
    fp = file(filename, 'wb')
    print ('打开文件'.decode("utf-8"))
    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行情况：')
    #运行测试用例
    runner.run(testunit)
    fp.close()  #关闭报告文件
    #结束时间
    time_end=time.time()
    #定义路径
    dstdirname=os.path.dirname(os.getcwd())+'\\result\\excel'
    #汇总整理excel报告
    srcfile=dstdirname+"\\"+"ErrorReport.xls"
    srcfile1=dstdirname+"\\"+"FailureReport.xls"
    passfile=dstdirname+"\\"+"PassReport.xls"
    #  realpassfile=dstdirname+"\\"+"RelPassReport.xls"

    #总报告
    report=dstdirname+"\\"+"report.xls"
    dstfile=dstdirname+"\\"+"ResultReport_warning.xls"

    #整理出真正的relpassfile
    # write_represult.writepass(srcfile1,passfile,realpassfile)

    #将config下面的ResultReport.xls复制到 result/excel下面的文件
    srcconfigfile=[os.path.dirname(os.getcwd())+'\\config'+"\\"+"Android_warning.xls"]
    if not os.path.exists(dstfile):
        processfile.copy_files(srcconfigfile,dstdirname,dstfile)

    #将fail与error、pass写进总表,先写pass
    for filename in [passfile,srcfile,srcfile1]:
        if os.path.exists(filename):
            write_represult.writedata(filename,dstfile)

    #生成report表，正常生成时发送邮件
    try:
        write_summary.init(dstfile,report,time_start,time_end)
    except:
        pass
    else:
        smail().sendreport(report,dstfile,srcfile1)

    #压缩文件
    dstzip=os.path.dirname(os.getcwd())+'\\ZIP\\'+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"_"+"Report.zip"
    processfile.zip_dir(dstdirname,dstzip)

if __name__== "__main__":
    #开启定时任务
 #   print (u"定时任务开启-------测试执行任务将从%s时%s分开始执行----------------"%(readconfig.readscheconfig()[1],readconfig.readscheconfig()[0]))
    scheduler = BlockingScheduler()
  #  scheduler.add_job(do_testunit,'cron', minute=readconfig.readscheconfig()[0], hour=readconfig.readscheconfig()[1])mon,tue,wed,thu,fri,sat,sun
    scheduler.add_job(do_testunit,'cron', day_of_week='mon',hour=14,minute=05)
    print('Press Ctrl+C to exit')
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass