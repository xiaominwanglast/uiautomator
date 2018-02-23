#coding:utf-8

import sys
import time
import os
import shutil
from PIL import Image
sys.path.append (r"..")

from apptest.PO import  BasePage
from apptest.PO import VideoPage
from apptest.PO import Superunit
from apptest.Public.getmethodname  import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from random import randint

class nologin_video(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\video\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    body1=u"视频>新闻信息流>UI>未登录>UI检查-空白页"
    body2=u"视频>视频内页>UI>未登录>UI检查-空白页"
    def test_01_video(self):
        u"""视频信息流UI测试"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        getpindao(self.driver)
        for i in range(1):
            BasePage.Base(self.driver).do_swipe(self.driver,"up")
            try:
                self.assertTrue(VideoPage.Video(self.driver).find_video_cover())
                self.assertTrue(VideoPage.Video(self.driver).find_video_title())
            except:
                print (u"视频信息流>UI>检查信息流数据-空白页")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body1)


    def test_02_invideos(self):
        u"""视频内页信息流UI测试"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        getpindao(self.driver)
        VideoPage.Video(self.driver).click_videonone()
        #流量4G卡会提示出现这个问题
        try:
            VideoPage.Video(self.driver).click_tvconfirm()
        except:
            pass
        try:
            self.assertTrue(VideoPage.Video(self.driver).find_tv_titles())
        except:
            print (u"进入视频内页异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body2)


def getpindao(driver):
    time.sleep(3)
    VideoPage.Video(driver).click_video_entry()
    time.sleep(5)
    VideoPage.Video(driver).find_videotip()[randint(0,5)].click()



