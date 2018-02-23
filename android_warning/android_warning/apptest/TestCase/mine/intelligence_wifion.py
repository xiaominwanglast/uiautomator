#coding:utf-8

from apptest.PO import Superunit
from apptest.PO import MinePage
from apptest.Public.getmethodname import GetName
from apptest.PO import BasePage
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
import os ,time
from PIL import Image
from apptest.PO import VideoPage
from apptest.PO import NewsPage
from apptest.PO import LoginPage
from apptest.PO import CollectPage
from apptest.PO import SetPage
from random import  randint
from apptest.Public import processfile
from apptest.PO import channel
from apptest.PO import SearchPage
#手机号另行登陆测试
class intelligent(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    def test_01_intel(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        BasePage.Base(self.driver).do_swipe(self.driver,"up")
        MinePage.Mine(self.driver).click_noimage()
        NewsPage.News(self.driver).click_news_entry()
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
            self.assertTrue(NewsPage.News(self.driver).find_nums())
        except:
            BasePage.Base(self.driver).do_swipe(self.driver,"smallup")
        try:
            self.assertTrue(NewsPage.News(self.driver).find_nums())
            CollectPage.Collect(self.driver).click_favorite_image()
        except:
            print (u"智能无图-WIFI>进入美女栏位-显示异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"智能无图-WIFI>进入美女栏位-显示异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        VideoPage.Video(self.driver).click_video_entry()
        BasePage.Base(self.driver).do_swipe(self.driver,"down")
        try:
            self.assertTrue( VideoPage.Video(self.driver).find_video_cover())
            CollectPage.Collect(self.driver).click_video_save()
        except:
            print (u"智能无图-WIFI>进入视频页面-显示异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"智能无图-WIFI>进入视频页面-显示异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        else:
            CollectPage.Collect(self.driver).click_mine()
            CollectPage.Collect(self.driver).click_mine_collect()
            CollectPage.Collect(self.driver).click_tv_video()
        try:
            self.assertTrue( VideoPage.Video(self.driver).find_video_cover())
        except:
            print (u"智能无图-WIFI>收藏界面-视频异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"智能无图-WIFI>收藏界面-视频异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        self.driver.back()
        BasePage.Base(self.driver).do_swipe(self.driver,"up")
        MinePage.Mine(self.driver).click_noimage()