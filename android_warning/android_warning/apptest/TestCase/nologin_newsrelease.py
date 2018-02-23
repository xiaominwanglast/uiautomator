#coding:utf-8
import random
import sys
import time
import os
import unittest
from random import choice
sys.path.append (r"..")

from apptest.PO import Superunit
from apptest.Public.getmethodname  import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.PO import NewsPage
from apptest.PO import BasePage
from apptest.PO import channel
from apptest.PO import SearchPage

#新闻内页>关闭新闻内页
#1.新闻>信息流>频道（随机取）>点击任意新闻标题>进入新闻内页>上拉页面到当前页面返回顶部
#2.新闻>信息流>频道（随机取）>点击任意新闻标题>进入新闻内页>点击“返回”按钮

class nologin_newsclose(Superunit.initunit):
    work_path = os.path.dirname(os.getcwd())+"\\screen\\nologin\\news\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_newsrelease(self):
        name1=self.__class__.__name__ +'.'+GetName.get_current_function_name()
        channel.channelele(self.driver).click_edit_addchannel()
        mine=channel.channelele(self.driver).allindex()
        chan=choice(mine[1])
        print(u"随机选择我的频道-%s"%chan)
        self.driver.find_element_by_name("%s"%chan).click()
        time.sleep(3)
        NewsPage.News(self.driver).click_topic()
        BasePage.Base(self.driver).do_swipe(self.driver,"down")
        try:
            self.assertTrue(self.driver.find_element_by_name("%s"%chan))
            select=channel.channelele(self.driver).select_channel()
            self.assertEqual(select,chan)
        except:
            print (u"新闻内页释放出现异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body1=u"新闻内页释放出现异常"
            smail().send_errormsg(str(filename),body1,self.work_path)

    def test_02_newsback(self):
        name1=self.__class__.__name__ +'.'+GetName.get_current_function_name()
        channel.channelele(self.driver).click_edit_addchannel()
        mine=channel.channelele(self.driver).allindex()
        chan=choice(mine[1])
        print(u"随机选择我的频道-%s"%chan)
        self.driver.find_element_by_name(chan).click()
        time.sleep(3)
        NewsPage.News(self.driver).click_topic()
        self.driver.back()
        try:
            self.assertTrue(self.driver.find_element_by_name("%s"%chan))
            select=channel.channelele(self.driver).select_channel()
            self.assertEqual(select,chan)
        except:
            print (u"新闻内页返回出现异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body1=u"新闻内页返回出现异常"
            smail().send_errormsg(str(filename),body1,self.work_path)


if __name__=="__main__":
    unittest.main()