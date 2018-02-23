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
from apptest.PO import VideoPage

class videorefrash(Superunit.initunit):
    work_path = os.path.dirname(os.getcwd())+"\\screen\\video\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    def test_01_refrash(self):
        name1=self.__class__.__name__ +'.'+GetName.get_current_function_name()
        VideoPage.Video(self.driver).click_video_entry()
        VideoPage.Video(self.driver).find_videotip()[random.randint(0,5)].click()
        time.sleep(4)
        title=VideoPage.Video(self.driver).find_video_title()
        title_text=title.text
        BasePage.Base(self.driver).do_swipe(self.driver,"down")
        time.sleep(4)
        title1=VideoPage.Video(self.driver).find_video_title()
        title1_text=title1.text
        try:
            self.assertNotEqual(title_text,title1_text)
        except:
            print (u"视频频道>视频刷新及提示>下拉或点击悬浮-界面异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"视频频道>视频刷新及提示>下拉或点击悬浮-界面异常"
            smail().send_errormsg(str(filename),body,self.work_path)

    def test_02_invideo(self):
        name1=self.__class__.__name__ +'.'+GetName.get_current_function_name()
        VideoPage.Video(self.driver).click_video_entry()
        try:
            VideoPage.Video(self.driver).click_videonone()
            self.assertTrue(VideoPage.Video(self.driver).find_tv_titles())
            self.assertTrue(VideoPage.Video(self.driver).find_video_title())
            for i in range(5):
                BasePage.Base(self.driver).do_swipe(self.driver,"up")
            self.assertTrue(VideoPage.Video(self.driver).find_tvcommand())
            self.assertTrue(VideoPage.Video(self.driver).find_tvusername())
        except:
            print (u"视频频道>视频内页>视频内页（视频+相关视频+评论-界面异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"视频频道>视频内页>视频内页（视频+相关视频+评论-界面异常"
            smail().send_errormsg(str(filename),body,self.work_path)










