#coding:utf-8
import random
import sys
import time
import os
import unittest
sys.path.append (r"..")

from apptest.PO import channel
from apptest.PO import Superunit
from apptest.Public.getmethodname  import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.PO.BasePage import Base
from appium.webdriver.common.touch_action import TouchAction
#新闻频道管理>频道调整
#1.新闻>右上角“+”进入频道管理＞我的频道>长按除了头条和滚动以外的任意频道，拖动到除第一第二位的任意位置
#2.点击返回按钮，查看频道列表

class nologin_channeladjust(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\channel\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_adjustchannel(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        #初始化数组
        self.add=[]
        self.nextadd=[]
        channel.channelele(self.driver).click_edit_addchannel()
        # 开始遍历元素
        all=channel.channelele(self.driver).allindex()
        self.a=all[0]
        #遍历当前我的频道的元素放入到add的列表中
        b1=channel.channelele(self.driver).find_channel_name()
        for m in range(0,self.a-2):
            self.add.append(b1[m].text)
        count=random.sample(range(2,self.a-1),2)
        j=count[0]
        #准备点击拖拽的频道
        channel.channelele(self.driver).click_edit_channel()
        self.drag1=channel.channelele(self.driver).indexone(j)
        #拖拽到的位置频道
        self.drag2=channel.channelele(self.driver).indexone(count[1])
        print (u"准备拖拽的频道为第%d位频道-%s"%(j+1,self.add[j-1]))
        self.driver.drag_and_drop(self.drag1,self.drag2)
        time.sleep(3)
        channel.channelele(self.driver).click_edit_channel()
        b2=channel.channelele(self.driver).find_channel_name()
        for n in range(0,self.a-2):
            self.nextadd.append(b2[n].text)
        print (u"拖拽完成后现在第%d位频道-%s"%(j+1,self.nextadd[j-1]))
        try:
            self.assertNotEqual(self.add[j-1],self.nextadd[j-1])
        except:
            print (u"频道不能成功拖动出现异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"频道不能成功拖动出现异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        else:
            nologin_channeladjust.back(self.driver,j,self.nextadd[j-1],name1)

    @classmethod
    def back(self,driver,k,z,name1):
        self.driver=driver
        self.name=name1
        aa=''
        channel.channelele(self.driver).click_channel_back()
        #返回到新闻频道判断显示状态
        print (u"-----------开始向右滑动查找频道------------")
        for x in range(0,k):
            Base(self.driver).do_swipe(self.driver,"left")
        time.sleep(5)
        uiele=channel.channelele(self.driver).classname(k)
        if(uiele.is_selected()):
            pass
        else:
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body2=u"频道编辑后返回处于的位置异常"
            smail().send_errormsg(str(filename),body2,self.work_path)
        uiele2=channel.channelele(self.driver).find_tv()
        for ii in range(0,5):
            if(uiele2[ii].is_selected()):
                aa=uiele2[ii].text
                print (u"当前点亮频道为-%s"%aa)
        if (aa == z):
            pass
        else:
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body3=u"频道显示异常"
            smail().send_errormsg(str(filename),body3,self.work_path)


if __name__=="__main__":
    unittest.main()
