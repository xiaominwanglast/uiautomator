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
from apptest.PO.adbUtils import ADB

#新闻信息流>地名频道
#1.进入新闻页>地名频道（如：北京），检查频道内容
#2.点击天气概要图片位置
#3.点击返回箭头
#4.点击定位图标，展示城区列表后选择任意城区>返回
#5.刷新信息流

class nologin_placechannel(Superunit.initunit):
    work_path = os.path.dirname(os.getcwd())+"\\screen\\nologin\\news\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_placechose(self):
        name1=self.__class__.__name__ +'.'+GetName.get_current_function_name()
        channel.channelele(self.driver).click_edit_addchannel()
        placename=u"西安"
        try:
            self.driver.find_element_by_name("%s"%placename).click()
            time.sleep(3)
        except:
            print (u"需要订阅%s频道"%placename)
            channel.channelele(self.driver).click_channel_back()
            SearchPage.Search(self.driver).click_entry()
            SearchPage.Search(self.driver).input_keywords("%s"%placename)
            SearchPage.Search(self.driver).click_btn_search()
            SearchPage.Search(self.driver).click_subscribe_btn()
            NewsPage.News(self.driver).click_news_entry()
            self.driver.find_element_by_name("%s"%placename).click()
        try:
            self.assertTrue(NewsPage.News(self.driver).find_des())
        except:
            print(u"此频道已打开过，不能显示天气信息")
        else:
            print (u'此频道为首次打开，进行天气情况测试')
            try:
                #测试地方频道首次打开的天气显示是否正常
                self.assertTrue(NewsPage.News(self.driver).find_location())
                self.assertTrue(NewsPage.News(self.driver).find_temperature())
                self.assertTrue(NewsPage.News(self.driver).find_temperaturerange())
            except:
                print (u"地方频道天气出现异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body1=u"地方频道天气出现异常"
                smail().send_errormsg(str(filename),body1,self.work_path)
            else:
                #测试点击天气概要图片后显示的界面
                NewsPage.News(self.driver).click_temperature()
                try:
               #     self.assertTrue(NewsPage.News(self.driver).find_reflash())
               #     self.assertTrue(NewsPage.News(self.driver).find_titletext())
                    self.driver.find_element_by_class_name("android.view.View")
                except:
                    print (u"地方频道打开天气出现异常")
                    filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                    body2=u"地方频道打开天气出现异常"
                    smail().send_errormsg(str(filename),body2,self.work_path)

                #测试返回后显示是否正常
                self.driver.back()
                try:
                    self.assertTrue(NewsPage.News(self.driver).find_location())
                    self.assertTrue(NewsPage.News(self.driver).find_temperature())
                    self.assertTrue(NewsPage.News(self.driver).find_temperaturerange())
                    self.assertTrue(NewsPage.News(self.driver).find_des())
                    self.assertTrue(NewsPage.News(self.driver).find_topic())
                except:
                    print (u"地方频道打开天气出现异常")
                    filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                    body3=u"地方频道打开天气出现异常"
                    smail().send_errormsg(str(filename),body3,self.work_path)
                else:
                    #测试点击定位图标，展示城区列表后选择任意城区>返回
                    NewsPage.News(self.driver).click_location()
                    ele=NewsPage.News(self.driver).find_cityname()
                    print (u"点击城市列表内-%s"%ele[1].get_attribute('name'))
                    ele[1].click()
                    try:
                        self.assertTrue(NewsPage.News(self.driver).find_location())
                        self.assertTrue(NewsPage.News(self.driver).find_temperature())
                        self.assertTrue(NewsPage.News(self.driver).find_temperaturerange())
                        self.assertTrue(NewsPage.News(self.driver).find_des())
                    except:
                        print (u"切换地名后天气出现异常")
                        filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                        body4=u"切换地名后天气出现异常"
                        smail().send_errormsg(str(filename),body4,self.work_path)
                #刷新信息
                BasePage.Base(self.driver).do_swipe(self.driver,"down")
                try:
                    self.assertFalse(NewsPage.News(self.driver).find_dess())
                except:
                    print (u"刷新后天气出现异常")
                    filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                    body4=u"刷新后天气出现异常"
                    smail().send_errormsg(str(filename),body4,self.work_path)


if __name__=="__main__":
    unittest.main()
