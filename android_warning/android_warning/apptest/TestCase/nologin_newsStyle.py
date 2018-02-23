#coding:utf-8
import random
import sys
import time
import os
import unittest
sys.path.append (r"..")

from apptest.PO import Superunit
from apptest.Public.getmethodname  import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.PO import NewsPage
from apptest.PO import BasePage

#新闻信息流>样式
#1.信息流正常展示大图，三图、单图和视频新闻；(这条由于UI框架不识别，所以暂时先搁置)
# 信息流中部分新闻显示热门、推荐、暖文、视频等标签；广告显示广告标签（与H5页一致）
class nologin_NewsStyle(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\news\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_style(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        NewsPage.News(self.driver).click_news_entry()
        list1=[u"热门",u"推荐",u"视频"]
        lista=do_collectlist(self.driver)
        BasePage.Base(self.driver).do_swipe(self.driver,"down")
        listb=list(set(lista).union(set(do_collectlist(self.driver))))
        BasePage.Base(self.driver).do_swipe(self.driver,"up")
        listc=list(set(listb).union(set(do_collectlist(self.driver))))
        #两个list求交集
        if list(set(listc).intersection(set(list1))):
            print (u"信息流中有热文\推荐\视频标签")
        else:
            print (u"信息流中没有热文\推荐\视频标签")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"信息流中没有热文\推荐\视频标签"
            smail().send_errormsg(str(filename),body,self.work_path)




def do_collectlist(driver):

    list1=[list2.get_attribute('name') for  list2 in driver.find_elements_by_class_name("android.widget.TextView")]

    return  list1


if __name__=="__main__":
    unittest.main()

