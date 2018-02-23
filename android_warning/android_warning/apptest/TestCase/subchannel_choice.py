#coding:utf-8

import sys
import time
import os
import unittest
sys.path.append (r"..")

from apptest.PO import nicechoice
from apptest.PO import BasePage
from apptest.PO import SearchPage
from apptest.PO import Superunit
from apptest.Public.getmethodname  import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.PO import channel
from apptest.PO import NewsPage
from apptest.PO import DiscoveryPage

class sub_choice(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\subchannel\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_subchoice(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        channel.channelele(self.driver).click_edit_addchannel()
        channel.channelele(self.driver).click_add_channel()
        try:
            self.assertTrue(nicechoice.choose(self.driver).find_texttitle())
            self.assertTrue(nicechoice.choose(self.driver).find_textdetail())
            self.assertTrue(nicechoice.choose(self.driver).find_category())
            self.assertTrue(nicechoice.choose(self.driver).find_textsub())
        except:
            print (u"1)展示精选订阅频道页面异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"1)展示精选订阅频道页面异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        name=u"苹果"
        for i in range(2):
            channel.channelele(self.driver).click_channel_back()
        DiscoveryPage.Discovery(self.driver).click_foundentry()
        nicechoice.choose(self.driver).click_choice()
        try:
            self.assertTrue(nicechoice.choose(self.driver).find_texttitle())
            self.assertTrue(nicechoice.choose(self.driver).find_textdetail())
            self.assertTrue(nicechoice.choose(self.driver).find_category())
            self.assertTrue(nicechoice.choose(self.driver).find_textsub())
        except:
            print (u"2)展示精选订阅频道页面异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body1=u"2)展示精选订阅频道页面异常"
            smail().send_errormsg(str(filename),body1,self.work_path)
        nicechoice.choose(self.driver).click_layoutsearch()
        SearchPage.Search(self.driver).input_keywords(name)
        SearchPage.Search(self.driver).click_btn_search()
        SearchPage.Search(self.driver).click_subscribe_btn()
        SearchPage.Search(self.driver).click_subscribe_back()
        NewsPage.News(self.driver).click_news_entry()
        self.driver.find_element_by_name(name).click()
        list=[u"水果",u"甜"]
        contentlist=NewsPage.News(self.driver).topic_list()
        for i in contentlist:
            for j in list:
                if j in i:
                    print (u"精准搜索框>输入关键词>苹果>和日常水果苹果内容无关联-异常")
                    filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                    body2=u"精准搜索框>输入关键词>苹果>和日常水果苹果内容无关联-异常"
                    smail().send_errormsg(str(filename),body2,self.work_path)
        NewsPage.News(self.driver).click_news_entry()
        channel.channelele(self.driver).click_edit_addchannel()
        channel.channelele(self.driver).click_edit_channel()
        self.driver.find_element_by_name(name).click()
        channel.channelele(self.driver).click_edit_channel()
if __name__=="__main__":
    unittest.main()
