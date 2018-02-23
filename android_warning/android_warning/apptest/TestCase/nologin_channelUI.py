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


#新闻频道管理>频道管理页UI
#1.展示频道管理页面，显示我的频道和推荐频道模块
#2.返回到新闻首页，上一次查看的频道栏位

class nologin_channelUI(Superunit.initunit):
    work_path =os.path.dirname(os.getcwd())+"\\screen\\nologin\\channel\\"+time.strftime("%Y+%m+%d",time.localtime(time.time()))
    body1=u"新闻>新闻频道管理>UI>未登录>UI检查-空白页"
    def test_01_UI(self):
        u"""频道管理页面UI测试"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        channel.channelele(self.driver).click_edit_addchannel()
        try:
            self.assertTrue(channel.channelele(self.driver).find_mine_channel())
            self.assertTrue(channel.channelele(self.driver).find_suggest_channel())
            self.assertTrue(channel.channelele(self.driver).find_channel_name())
        except:
            print(u"新闻频道管理>UI>检查频道管理页面-空白页")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body1)


if __name__=="__main__":
    unittest.main()