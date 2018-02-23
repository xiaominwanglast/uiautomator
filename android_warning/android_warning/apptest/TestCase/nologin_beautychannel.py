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
from apptest.PO import channel
from apptest.PO import SearchPage
#from appium.webdriver.connectiontype import ConnectionType
#新闻信息流>美女频道
#1.进入新闻页>美女频道
#2.点击图片>进入全屏浏览>左右切换图片
#3.点击返回按钮>返回美女信息流>点赞或倒彩（互斥）>查看页面数据变化

class nologin_beauty(Superunit.initunit):
    work_path = os.path.dirname(os.getcwd())+"\\screen\\nologin\\news\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_beauty(self):
        name1=self.__class__.__name__ +'.'+GetName.get_current_function_name()
        channel.channelele(self.driver).click_edit_addchannel()
        try:
            self.driver.find_element_by_name(u"美女").click()
            time.sleep(3)
        except:
            print (u"需要订阅美女频道")
            self.driver.back()
            SearchPage.Search(self.driver).click_entry()
            SearchPage.Search(self.driver).input_keywords(u"美女")
            SearchPage.Search(self.driver).click_btn_search()
            SearchPage.Search(self.driver).click_subscribe_btn()
            NewsPage.News(self.driver).click_news_entry()
            self.driver.find_element_by_name(u"美女").click()
        try:
            NewsPage.News(self.driver).find_picture()
            NewsPage.News(self.driver).find_topic()
            select=channel.channelele(self.driver).select_channel()
            self.assertEqual(select,u"美女")
            BasePage.Base(self.driver).do_swipe(self.driver,"smallup")
            self.assertTrue(NewsPage.News(self.driver).find_kan())
            self.assertTrue(NewsPage.News(self.driver).find_zan())
            self.assertTrue(NewsPage.News(self.driver).find_cai())
            self.assertTrue(NewsPage.News(self.driver).find_favorite())
            self.assertTrue(NewsPage.News(self.driver).find_share())
            ele=NewsPage.News(self.driver).find_nums().get_attribute('name')
            self.assertEqual(ele[-1],u"图")
        except:
            print (u"美女频道出现异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body1=u"删除自定义频道返回后仍然存在，出现异常"
            smail().send_errormsg(str(filename),body1,self.work_path)

    def test_02_allbeauty(self):
        name1=self.__class__.__name__ +'.'+GetName.get_current_function_name()
        channel.channelele(self.driver).click_edit_addchannel()
        self.driver.find_element_by_name(u"美女").click()
        time.sleep(3)
        try:
            self.assertTrue(NewsPage.News(self.driver).find_nums())
        except:
            BasePage.Base(self.driver).do_swipe(self.driver,"smallup")
        ele=NewsPage.News(self.driver).find_nums().get_attribute('name')
        NewsPage.News(self.driver).click_nums()
        if (BasePage.Base(self.driver).webstate()=="WIFI_ONLY"):
            '''
            try:
                time.sleep(3)
                self.driver.find_element_by_xpath("//android.view.View[@content-desc=\'1 / %s\']"%(int(ele[:-1])+1))
            except:
                print (u"全图观看美女图片数量出现异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body1=u"全图观看美女图片数量出现异常"
                smail().send_errormsg(str(filename),body1,self.work_path)
            else:
            '''
            for i in range(3):
                try:
                    #异常 图片不能加载
                    BasePage.Base(self.driver).do_swipe(self.driver,"left")
                    self.driver.find_element_by_name(u"加载失败，点击重试")
                    print (u"全图观看美女图片出现异常")
                    filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                    body2=u"全图观看美女图片出现异常"
                    smail().send_errormsg(str(filename),body2,self.work_path)
                    break
                except:
                    pass
            for i in range(3):
                try:
                    #异常 图片link有问题
                    BasePage.Base(self.driver).do_swipe(self.driver,"right")
                    self.driver.find_element_by_xpath("//android.view.View[@content-desc=' could not be loaded.']")
                    print (u"全图观看美女图片出现异常")
                    filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                    body3=u"全图观看美女图片出现异常"
                    smail().send_errormsg(str(filename),body3,self.work_path)
                    break
                except:
                    pass

    def test_03_zanANDcai(self):
        name1=self.__class__.__name__ +'.'+GetName.get_current_function_name()
        channel.channelele(self.driver).click_edit_addchannel()
        self.driver.find_element_by_name(u"美女").click()
        try:
            self.assertTrue(NewsPage.News(self.driver).find_zan())
        except:
            BasePage.Base(self.driver).do_swipe(self.driver,"smallup")
        zan=NewsPage.News(self.driver).find_zan()
        cai=NewsPage.News(self.driver).find_cai()
        #先点的赞，赞+1,再点击菜互斥不加1
        NewsPage.News(self.driver).click_zan()
        NewsPage.News(self.driver).click_cai()
        zan1=NewsPage.News(self.driver).find_zan()
        cai1=NewsPage.News(self.driver).find_cai()
        if int(zan.text)==int(zan1.text):
            print (u"图片已经赞过，不能再赞")
        else:
            try:
                self.assertEqual(int(zan.text)+1,int(zan1.text))
                self.assertEqual(int(cai.text),int(cai1.text))
            except:
                print (u"点赞美女图片出现异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body1=u"点赞美女图片出现异常"
                smail().send_errormsg(str(filename),body1,self.work_path)

if __name__==" __main__":
    unittest.main()



