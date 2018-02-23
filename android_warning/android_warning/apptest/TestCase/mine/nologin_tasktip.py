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


class nologin_tasknotify(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_notify(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        MinePage.Mine(self.driver).click_task()
        try:
            TaskCenterPage.taskcenter(self.driver).click_iv_close()
        except:
            pass
        self.driver.back()
        try:
            self.assertTrue(MinePage.Mine(self.driver).find_tasknotify())
        except:
            print (u"任务中心>右侧提示>3个任务未完成-显示异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"任务中心>右侧提示>3个任务未完成-显示异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        MinePage.Mine(self.driver).click_task()
        BasePage.Base(self.driver).do_swipe(self.driver,"smallup")
        e=TaskCenterPage.taskcenter(self.driver).find_tvdetails()
        try:
            self.assertTrue(TaskCenterPage.taskcenter(self.driver).find_dailystate())
            for i in range(3):
                self.assertEqual(int((e[i].text)[0]),0)
        except:
            print (u"任务中心>未完成每个任务均显示0/X-显示异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"任务中心>未完成每个任务均显示0/X-显示异常"
            smail().send_errormsg(str(filename),body,self.work_path)