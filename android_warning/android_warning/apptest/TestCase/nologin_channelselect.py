#coding:utf-8
import random
import sys
import time
import os
import unittest
sys.path.append (r"..")

from apptest.PO import channel
from apptest.PO import Superunit
from apptest.Public.getmethodname  import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.PO.BasePage import Base
from apptest.PO import NewsPage
#新闻频道>频道切换;
# 1.新闻>点击频道名称
# 2.新闻>左右滑动页面

class nologin_channelselect(Superunit.initunit):
#class nologin_serach(unittest.TestCase):

    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\channel\\select\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_newsChannel(self):
        u"""测试新闻频道选择"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        channel.channelele(self.driver).click_news_enter()
        channel.channelele(self.driver).find_tv()[random.randint(1,5)].click()
        select= channel.channelele(self.driver).select_channel()
        if (select !=u"头条"):
            print (u"已选择%s"%select)
        else:
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"频道未被选中"
            smail().send_errormsg(str(filename),body,self.work_path)
    def test_02_rightleft(self):
        u"""测试新闻左右滑动"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        #向右滑动
        topic1=NewsPage.News(self.driver).find_topic()
        for j in range(3):
            Base(self.driver).do_swipe(self.driver,"left")
        selectleft=channel.channelele(self.driver).select_channel()
        topic2=NewsPage.News(self.driver).find_topic()
        try:
            self.assertNotEqual(selectleft,u"头条")
            self.assertNotEqual(topic1,topic2)
        except:
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"新闻>左右滑动页面-出现异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        #向右滑动
        for j in range(3):
            Base(self.driver).do_swipe(self.driver,"left")
        selectleft1=channel.channelele(self.driver).select_channel()
        topic3=NewsPage.News(self.driver).find_topic()
        try:
            self.assertNotEqual(selectleft,selectleft1)
            self.assertNotEqual(topic3,topic2)
        except:
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"新闻>左右滑动页面-出现异常"
            smail().send_errormsg(str(filename),body,self.work_path)

        #向左滑动
        for j in range(3):
            Base(self.driver).do_swipe(self.driver,"right")
        selectright1=channel.channelele(self.driver).select_channel()
        topic4=NewsPage.News(self.driver).find_topic()
        try:
            self.assertNotEqual(selectright1,selectleft1)
            self.assertNotEqual(topic3,topic4)
        except:
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"新闻>左右滑动页面-出现异常"
            smail().send_errormsg(str(filename),body,self.work_path)

if __name__=="__main__":
    unittest.main()
