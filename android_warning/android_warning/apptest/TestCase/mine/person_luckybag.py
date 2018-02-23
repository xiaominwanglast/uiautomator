#coding:utf-8

import random
from apptest.PO import Superunit
from apptest.PO import  TaskCenterPage
from apptest.PO import  BasePage
from apptest.PO import  MinePage
from apptest.PO import  SearchPage
from apptest.Public.getmethodname import GetName
from apptest.PO import  NewsPage
from apptest.PO import  InsideNewsPage
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
import os ,time
from apptest.PO.adbUtils import ADB
from apptest.PO import nicechoice
from apptest.PO import channel
import unittest
class luckybag(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_firstcleardata(self):
        MinePage.Mine(self.driver).click_mine_entry()
        print(u"清理缓存")
        ADB().clearAppData(ADB().getCurrentPackageName())

    def test_02_nologin(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        MinePage.Mine(self.driver).click_task()
        try:
            TaskCenterPage.taskcenter(self.driver).click_iv_close()
            self.assertTrue(TaskCenterPage.taskcenter(self.driver).find_luckybag())
        except:
            print (u"任务中心>新人福袋奖励未登录>提示-异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"任务中心>新人福袋奖励未登录>提示-异常"
            smail().send_errormsg(str(filename),body,self.work_path)

    def test_03_checkluckybag(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        MinePage.Mine(self.driver).click_task()
        try:
            TaskCenterPage.taskcenter(self.driver).click_iv_close()
            print (u"任务中心>新人福袋奖励再次登陆>提示-异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"任务中心>新人福袋奖励再次登陆>提示-异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        except:
            pass
        try:
            self.assertTrue(TaskCenterPage.taskcenter(self.driver).find_luckybag())
            print (u"任务中心>新人福袋奖励再次登陆>提示-异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"任务中心>新人福袋奖励再次登陆>提示-异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        except:
            pass
if __name__=="__main__":
    unittest.main()