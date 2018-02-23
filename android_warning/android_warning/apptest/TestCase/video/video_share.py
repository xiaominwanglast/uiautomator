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

class videoshare(Superunit.initunit):
    work_path = os.path.dirname(os.getcwd())+"\\screen\\video\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    def test_01_share(self):
        name1=self.__class__.__name__ +'.'+GetName.get_current_function_name()
        VideoPage.Video(self.driver).click_video_entry()
        VideoPage.Video(self.driver).click_comment()
        time.sleep(15)
        try:
            self.assertTrue(VideoPage.Video(self.driver).find_tvshare())
        except:
            time.sleep(10)
        else:
            VideoPage.Video(self.driver).click_tvshare()
            VideoPage.Video(self.driver).click_pengyouquan()
            try:
                VideoPage.Video(self.driver).click_fasong()
                self.assertTrue(VideoPage.Video(self.driver).find_video_title())
            except:
                print (u"视频栏位>视频新闻>点击分享按钮>选择微信朋友圈分享新闻-界面异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"视频栏位>视频新闻>点击分享按钮>选择微信朋友圈分享新闻-界面异常"
                smail().send_errormsg(str(filename),body,self.work_path)
            VideoPage.Video(self.driver).click_tvshare()
            VideoPage.Video(self.driver).click_weixin()
            try:
                VideoPage.Video(self.driver).click_make()
                VideoPage.Video(self.driver).click_name()
                VideoPage.Video(self.driver).click_sure()
                VideoPage.Video(self.driver).click_share()
                VideoPage.Video(self.driver).click_backdf()
            except:
                print (u"视频栏位>视频新闻>点击分享按钮>选择微信好友-界面异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"视频栏位>视频新闻>点击分享按钮>选择微信好友-界面异常"
                smail().send_errormsg(str(filename),body,self.work_path)
            time.sleep(5)
            VideoPage.Video(self.driver).click_tvshare()
            VideoPage.Video(self.driver).click_qq()
            try:
                VideoPage.Video(self.driver).click_minepc()
                VideoPage.Video(self.driver).click_fasong()
                VideoPage.Video(self.driver).click_backdf()
            except:
                print (u"视频栏位>视频新闻>点击分享按钮>选择qq-界面异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"视频栏位>视频新闻>点击分享按钮>选择qq-界面异常"
                smail().send_errormsg(str(filename),body,self.work_path)
            time.sleep(5)
            VideoPage.Video(self.driver).click_tvshare()
            VideoPage.Video(self.driver).click_qzone()
            try:
                VideoPage.Video(self.driver).click_fabiao()
            except:
                print (u"视频栏位>视频新闻>点击分享按钮>选择qq空间-界面异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"视频栏位>视频新闻>点击分享按钮>选择qq空间-界面异常"
                smail().send_errormsg(str(filename),body,self.work_path)
            time.sleep(5)
            VideoPage.Video(self.driver).click_tvshare()
            VideoPage.Video(self.driver).click_sina()
            try:
                VideoPage.Video(self.driver).click_fasong()
            except:
                print (u"视频栏位>视频新闻>点击分享按钮>选择新浪微博-界面异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"视频栏位>视频新闻>点击分享按钮>选择新浪微博-界面异常"
                smail().send_errormsg(str(filename),body,self.work_path)
            time.sleep(5)
            VideoPage.Video(self.driver).click_tvshare()
            try:
                VideoPage.Video(self.driver).click_clipboard()
                self.assertTrue(VideoPage.Video(self.driver).find_tvshare())
            except:
                print (u"视频栏位>视频新闻>点击分享按钮>选择复制链接-界面异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"视频栏位>视频新闻>点击分享按钮>选择复制链接-界面异常"
                smail().send_errormsg(str(filename),body,self.work_path)




