#coding:utf-8

import random
from apptest.PO import Superunit
from apptest.PO import  BasePage
from apptest.PO import  MinePage
from apptest.Public.getmethodname import GetName
from apptest.PO import  NewsPage
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
import os ,time
from apptest.PO import SetPage
class bodysize(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    def test_01_body(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        MinePage.Mine(self.driver).click_set()
        SetPage.Set(self.driver).click_bodysize()
        BasePage.Base(self.driver).tapxy(0.17,0.4,self.driver,2)
        BasePage.Base(self.driver).tapxy(0.84,0.66,self.driver,2)
        self.driver.back()
        NewsPage.News(self.driver).click_news_entry()
        small=NewsPage.News(self.driver).find_topic()
        num_small=small.size['height']
        MinePage.Mine(self.driver).click_mine_entry()
        MinePage.Mine(self.driver).click_set()
        SetPage.Set(self.driver).click_bodysize()
        BasePage.Base(self.driver).tapxy(0.17,0.52,self.driver,2)
        BasePage.Base(self.driver).tapxy(0.84,0.66,self.driver,2)
        self.driver.back()
        NewsPage.News(self.driver).click_news_entry()
        big=NewsPage.News(self.driver).find_topic()
        num_big=big.size['height']
        MinePage.Mine(self.driver).click_mine_entry()
        MinePage.Mine(self.driver).click_set()
        SetPage.Set(self.driver).click_bodysize()
        BasePage.Base(self.driver).tapxy(0.17,0.58,self.driver,2)
        BasePage.Base(self.driver).tapxy(0.84,0.66,self.driver,2)
        self.driver.back()
        NewsPage.News(self.driver).click_news_entry()
        verybig=NewsPage.News(self.driver).find_topic()
        num_verybig=verybig.size['height']
        MinePage.Mine(self.driver).click_mine_entry()
        MinePage.Mine(self.driver).click_set()
        SetPage.Set(self.driver).click_bodysize()
        BasePage.Base(self.driver).tapxy(0.17,0.46,self.driver,2)
        BasePage.Base(self.driver).tapxy(0.84,0.66,self.driver,2)
        self.driver.back()
        NewsPage.News(self.driver).click_news_entry()
        nomal=NewsPage.News(self.driver).find_topic()
        num_nomal=nomal.size['height']
        try:
            self.assertNotEqual(num_verybig,num_nomal)
            self.assertNotEqual(num_small,num_big)
            self.assertNotEqual(num_big,num_verybig)
        except:
            print (u"设置>字体调整-功能异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"设置>字体调整-功能异常"
            smail().send_errormsg(str(filename),body,self.work_path)

