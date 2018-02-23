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

class sub_loadnews(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\subchannel\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_loadnews(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        name=u"台湾"
    #    NewsPage.News(self.driver).click_news_entry()
        SearchPage.Search(self.driver).click_entry()
        SearchPage.Search(self.driver).input_keywords(name)
        SearchPage.Search(self.driver).click_btn_search()
        for i in range(3):
            try:
                self.assertTrue(SearchPage.Search(self.driver).find_topics())
                self.assertTrue(SearchPage.Search(self.driver).find_tvtime())
                BasePage.Base(self.driver).do_swipe(self.driver,"up")
            except:
                print (u"搜索>输入关键词搜索>搜索结果>上拉页面加载界面异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"搜索>输入关键词搜索>搜索结果>上拉页面加载界面异常"
                smail().send_errormsg(str(filename),body,self.work_path)
        for i in range(3):
            BasePage.Base(self.driver).do_swipe(self.driver,"down")
        try:
            SearchPage.Search(self.driver).click_subscribe_btn()
        except:
            pass
        else:
            NewsPage.News(self.driver).click_news_entry()
            self.driver.find_element_by_name(name).click()
            for i in range(3):
                try:
                    self.assertTrue(NewsPage.News(self.driver).find_topics())
                    BasePage.Base(self.driver).do_swipe(self.driver,"up")
                except:
                    print (u"订阅页面>订阅详情页>上拉页面加载界面异常")
                    filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                    body=u"订阅页面>订阅详情页>上拉页面加载界面异常"
                    smail().send_errormsg(str(filename),body,self.work_path)
            channel.channelele(self.driver).click_edit_addchannel()
            channel.channelele(self.driver).click_edit_channel()
            self.driver.find_element_by_name(name).click()
            channel.channelele(self.driver).click_edit_channel()
if __name__=="__main__":
    unittest.main()