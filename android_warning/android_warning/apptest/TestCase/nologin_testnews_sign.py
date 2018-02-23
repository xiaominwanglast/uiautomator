#coding:utf-8

import sys
import time
import os

import random

sys.path.append (r"..")
import unittest
from apptest.PO import  BasePage
from apptest.PO import NewsPage
from apptest.PO import Superunit
from apptest.PO import TaskCenterPage
from apptest.PO import LoginPage
from apptest.Public.getmethodname  import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.PO.adbUtils import ADB
from apptest.PO import MinePage
class nologin_news_sign(Superunit.initunit):
    work_path = os.path.dirname(os.getcwd())+"\\screen\\nologin\\news\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_firstcleardata(self):
        MinePage.Mine(self.driver).click_mine_entry()
        print(u"清理缓存")
        ADB().clearAppData(ADB().getCurrentPackageName())

    def test_02_back(self):
        name1=self.__class__.__name__ +'.'+GetName.get_current_function_name()
        try:
            self.assertTrue(NewsPage.News(self.driver).find_sign())
        except:
            print (u"清理缓存后没出现签标签出现异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"清理缓存后没出现签标签出现异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        else:
            sign=NewsPage.News(self.driver).find_sign()
            drop=NewsPage.News(self.driver).find_topics()
            self.driver.drag_and_drop(sign,drop[0])
            try:
                TaskCenterPage.taskcenter(self.driver).click_iv_close()
            except:
                pass
            try:
                TaskCenterPage.taskcenter(self.driver).find_login_el()
                TaskCenterPage.taskcenter(self.driver).find_tasktext()
            except:
                print (u"新闻页点击签到标签跳转任务中心出现异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"新闻页点击签到标签跳转任务中心出现异常"
                smail().send_errormsg(str(filename),body,self.work_path)
            else:
                self.driver.back()
                try:
                    self.assertFalse(NewsPage.News(self.driver).find_signs())
                except:
                    print (u"签到后还是出现签到标签出现异常")
                    filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                    body2=u"签到后还是出现签到标签出现异常"
                    smail().send_errormsg(str(filename),body2,self.work_path)

    def test_03_secondcleardata(self):
        MinePage.Mine(self.driver).click_mine_entry()
        print(u"清理缓存")
        ADB().clearAppData(ADB().getCurrentPackageName())

    def test_04_sign(self):
        name1=self.__class__.__name__ +'.'+GetName.get_current_function_name()
        try:
            self.assertTrue(NewsPage.News(self.driver).find_sign())
        except:
            pass
        else:
            NewsPage.News(self.driver).click_sign()
            try:
                TaskCenterPage.taskcenter(self.driver).click_iv_close()
            except:
                pass
            TaskCenterPage.taskcenter(self.driver).click_login_el()
            try:
                self.assertTrue(LoginPage.Login(self.driver).find_getcode())
                LoginPage.Login(self.driver).click_quicklogin()
            except:
                pass
            LoginPage.Login(self.driver).input_username("13262860620")
            LoginPage.Login(self.driver).input_password("wang12345")
            LoginPage.Login(self.driver).click_submit()
            try:
                TaskCenterPage.taskcenter(self.driver).click_login_el()
            except:
                pass
            try:
                e=TaskCenterPage.taskcenter(self.driver).find_signtoday_el()
                self.assertEqual(e[0],"+")
            except:
                print (u"新闻-签到出现异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body1=u"新闻-签到出现异常"
                smail().send_errormsg(str(filename),body1,self.work_path)
            else:
                self.driver.back()
                try:
                    self.assertFalse(NewsPage.News(self.driver).find_signs())
                except:
                    print (u"签到后还是出现签到标签出现异常")
                    filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                    body2=u"签到后还是出现签到标签出现异常"
                    smail().send_errormsg(str(filename),body2,self.work_path)

            self.driver.back()
            LoginPage.Login(self.driver).dologout()



if __name__=="__main__":
    unittest.main()