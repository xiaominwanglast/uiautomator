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

#新闻频道管理>频道添快选
#1.新闻>右上角“+”进入频道管理＞我的频道>点击任意频道
#1.页面跳转到新闻首页对应频道信息流页，频道名称高亮，信息流页面展示非空白
class nologin_channelquick(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\channel\\select\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_anychannel(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        #初始化数组
        channel.channelele(self.driver).click_edit_addchannel()
        all=channel.channelele(self.driver).allindex()
        self.add=all[1]
        j=random.randint(1,all[0]-1)
        channel.channelele(self.driver).click_indexone(j)
        print (u"随机点击的频道是%s"%self.add[j])
        select= channel.channelele(self.driver).select_channel()
        if (select==self.add[j]):
            print (u"%s频道处于选中点亮状态"%self.add[j])
        else:
            print (u"频道管理随机点击的频道未被点亮出现异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"频道管理随机点击的频道未被点亮出现异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        #判断点开的频道内页信息是否显示异常
        try:
            self.assertTrue(channel.channelele(self.driver).find_news_topic())
            print (u"信息流显示正常")
            time.sleep(2)
        except:
            print (u"信息流显示为空白页")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body1=u"信息流显示为空白页"
            smail().send_errormsg(str(filename),body1,self.work_path)

if __name__=="__main__":
    unittest.main()
