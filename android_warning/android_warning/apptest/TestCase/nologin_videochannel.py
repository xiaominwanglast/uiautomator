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

#新闻信息流>视频频道
#1.新闻>新闻信息流>点击播放视频
#2.点击视频位置或暂停标记
#3.点击全屏播放图标>再次点击播放
#4.左右滑动正播放的视频
#5.上下滑动调整播放声音
#6.点击非全屏图标
#7.播放视频过程中断网
#8.播放完毕检查播放图标

class nologin_videochannel(Superunit.initunit):
    work_path = os.path.dirname(os.getcwd())+"\\screen\\nologin\\news\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_videochannel(self):
        name1=self.__class__.__name__ +'.'+GetName.get_current_function_name()
        #体育频道视频多以体育频道为主
        channel.channelele(self.driver).click_edit_addchannel()
        video=channel.channelele(self.driver).allindex()
        if (u"体育" in video[1]):
            self.driver.find_element_by_name(u"体育").click()
        else:
            BasePage.Base(self.driver).do_swipe(self.driver,"up")
            self.driver.find_element_by_name(u"体育").click()
            BasePage.Base(self.driver).do_swipe(self.driver,"down")
            self.driver.find_element_by_name(u"体育").click()
        for i in range(25):
            try:
                ele=self.driver.find_elements_by_name(u"视频")
                self.assertTrue(len(ele)!=1)
                break
            except:
                BasePage.Base(self.driver).do_swipe(self.driver,"up")
        self.driver.find_element_by_name(u"视频").click()
        time.sleep(5)
        ele=NewsPage.News(self.driver).find_kvideo()
        for i in range(2):
            self.driver.tap([((ele.size)['width']/2,(ele.size)['height']/2)],1000)

        try:
            self.assertTrue(NewsPage.News(self.driver).find_videotitle())
            self.assertTrue(NewsPage.News(self.driver).find_tvtitle())
            self.assertTrue(NewsPage.News(self.driver).find_play())
            NewsPage.News(self.driver).click_full()
            self.assertTrue(NewsPage.News(self.driver).find_play())
            BasePage.Base(self.driver).tapxy(0.5,0.5,self.driver,6)
        except:
            print (u"点开的视频信息显示异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body1=u"全图观看美女图片出现异常"
            smail().send_errormsg(str(filename),body1,self.work_path)

if __name__=="__main__":
    unittest.main()


