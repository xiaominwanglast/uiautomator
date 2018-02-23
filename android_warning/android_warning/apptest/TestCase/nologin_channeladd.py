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

#新闻频道管理>频道添加
#1.被点击的频道进入我的频道末位且在频道推荐里消失
#2.选择的推荐频道显示在频道列表末位

class nologin_addchannel(Superunit.initunit):

    work_path =os.path.dirname(os.getcwd())+"\\screen\\nologin\\channel\\UI\\"+time.strftime("%Y+%m+%d",time.localtime(time.time()))

    def test_01_channelManage(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        channel.channelele(self.driver).click_edit_addchannel()
        #点击推荐频道
        onelist=channel.channelele(self.driver).allindex()
        suggestchannel=onelist[3]
        Base(self.driver).do_swipe(self.driver,"up")
        a=random.randint(0,onelist[2]-1)
        print (u"随机点击频道推荐-%s"%suggestchannel[a])
        self.driver.find_element_by_name(u"%s"%suggestchannel[a]).click()
        Base(self.driver).do_swipe(self.driver,"down")
        twolist=channel.channelele(self.driver).allindex()
        lentwo=twolist[0]
        try:
            self.assertTrue(suggestchannel[a] not in twolist[3])
            self.assertEqual(suggestchannel[a],twolist[1][lentwo-1])
            print (u"频道出现在我的频道末位并且在推荐频道已删除")
        except:
            print "error"
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"随机点击推荐频道没有添加到我的频道"
            smail().send_errormsg(str(filename),body,self.work_path)



    def test_02_channel(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        channel.channelele(self.driver).click_edit_addchannel()
        time.sleep(2)
        #我的频道总数
        all=channel.channelele(self.driver).allindex()
        self.a=all[0]
        channel.channelele(self.driver).click_indexone(self.a-1)
        time.sleep(3)
        te=channel.channelele(self.driver).classname(self.a-1)
        if(te.is_selected()):
            pass
        else:
            print(u"返回后选中频道出现异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"返回后选中频道出现异常"
            smail().send_errormsg(str(filename),body,self.work_path)


if __name__=="__main__":
    unittest.main()
