#coding:utf-8

import sys
import time
import os
import random

sys.path.append (r"..")

from apptest.PO import  BasePage
from apptest.PO import NewsPage
from apptest.PO import Superunit
from apptest.Public.getmethodname  import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.PO import InsideNewsPage
from random import randint
class nologin_news(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\news\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    body1=u"新闻>新闻信息流>UI>未登录>UI检查-空白页"
    body2=u"新闻>新闻内页>UI>未登录>UI检查-空白页"
    def test_01_newsview(self):
        u"""新闻信息流测试"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        getpindao(self.driver)
        #循环向上滑动页面，判断信息流是否显示正常
        for i in range(1):
            BasePage.Base(self.driver).do_swipe(self.driver,"up")
            try:
                self.assertTrue(NewsPage.News(self.driver).find_topic())
            except:
                print (u"新闻信息流>UI>检查信息流-空白页")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body1)

    # 判断信息流内页是否为空白页
    def test_02_innermsg(self):
        u"""新闻信息流内页测试"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        getpindao(self.driver)
        ele=NewsPage.News(self.driver).find_topics()
        ele[1].click()
        time.sleep(3)
      #  NewsPage.News(self.driver).click_topic()
        try:
            self.assertTrue(InsideNewsPage.Inside(self.driver).find_configloc() or InsideNewsPage.Inside(self.driver).find_configloc_other())
        except:
            print (u"新闻信息流>UI>新闻内页>检查信息流-空白页")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body2)

def getpindao(driver):
    NewsPage.News(driver).click_news_entry()
    time.sleep(5)
    list=[u"推荐",u"热点",u"社会",u"国内",u"国际",u"科技",u"健康",u"人文",u"娱乐",u"军事",u"体育",u"笑话",u"游戏",u"星座",u"时尚"]
    lista=NewsPage.News(driver).find_pindaos()[0:5]
    print ("--------------------------------")
    listb=[]
    for i in lista:
        if i.get_attribute('name')  in list:
             listb.append(i)
    for i in listb:
        print i.get_attribute('name')
    print ("----------------------------")
    if len(listb)==1:
        listb[0].click()
    else:
        listb[random.randint(0,len(listb)-1)].click()
    time.sleep(3)

