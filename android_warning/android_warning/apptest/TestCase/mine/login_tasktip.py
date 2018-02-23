#coding:utf-8

import random
from apptest.PO import Superunit
from apptest.PO import  TaskCenterPage
from apptest.PO import  BasePage
from apptest.PO import  MinePage
from apptest.PO import  HisreadPage
from apptest.Public.getmethodname import GetName
from apptest.PO import  NewsPage
from apptest.PO import  InsideNewsPage
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
import os ,time

class login_tasknotify(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_notify(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        a=MinePage.Mine(self.driver).find_tasknotifyID()
        num= int((a.text)[0])
        try:
            self.assertTrue(a.text in [u"3个任务未完成",u"2个任务未完成",u"1个任务未完成",u"赚积分换礼物"])
        except:
            print (u"任务中心>显示任务完成状态-显示异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"任务中心>显示任务完成状态-显示异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        MinePage.Mine(self.driver).click_task()
        BasePage.Base(self.driver).do_swipe(self.driver,"smallup")
        e=TaskCenterPage.taskcenter(self.driver).find_tvdetails()
        j=0
        for i in range(3):
            print ((e[i].text).split('/'))[0],((e[i].text).split('/'))[1]
            if int(((e[i].text).split('/'))[0]) != int(((e[i].text).split('/'))[1]):
                j=j+1
        if j!=0:
            try:
                self.assertEqual(num,j)
            except:
                print (u"任务中心>未完成数量和我的页面提示数量相同-显示异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"任务中心>未完成数量和我的页面提示数量相同-显示异常"
                smail().send_errormsg(str(filename),body,self.work_path)
        else:
            try:
                self.assertFalse(TaskCenterPage.taskcenter(self.driver).find_dailystate())
            except:
                print (u"任务中心>任务全部完成-显示异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"任务中心>任务全部完成-显示异常"
                smail().send_errormsg(str(filename),body,self.work_path)
