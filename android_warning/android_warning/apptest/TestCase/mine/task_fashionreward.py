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

class fashionUI(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_rewardUI(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        MinePage.Mine(self.driver).click_task()
        BasePage.Base(self.driver).do_swipe(self.driver,"up")
        try:
            TaskCenterPage.taskcenter(self.driver).click_fashion_shareread()
            self.assertTrue(TaskCenterPage.taskcenter(self.driver).find_fashion_shareread())
        except:
            print (u"我的>任务中心>达人奖励下点击分享被阅读-显示异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"我的>任务中心>达人奖励下点击分享被阅读-显示异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        self.driver.back()
        time.sleep(2)
        TaskCenterPage.taskcenter(self.driver).click_invitefs()
        try:
            TaskCenterPage.taskcenter(self.driver).click_qqspaceshare()
            TaskCenterPage.taskcenter(self.driver).click_fasong()
            TaskCenterPage.taskcenter(self.driver).click_invitefs()
            TaskCenterPage.taskcenter(self.driver).click_copynum()
            TaskCenterPage.taskcenter(self.driver).click_invitefs()
            TaskCenterPage.taskcenter(self.driver).click_inviterule()
            self.assertTrue(TaskCenterPage.taskcenter(self.driver).find_invitefs())
        except:
            print (u"我的>任务中心>达人奖励下点击邀请好友三种方式-异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"我的>任务中心>达人奖励下点击邀请好友三种方式-显示异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        self.driver.back()
        self.driver.back()