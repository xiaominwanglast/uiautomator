#coding:utf-8

import sys
import time
import os
import unittest
sys.path.append (r"..")

from apptest.PO import nicechoice
from apptest.PO import BasePage
from apptest.PO import SearchPage
from apptest.PO import Superunit
from apptest.Public.getmethodname  import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.PO import channel
from apptest.PO import NewsPage
from apptest.PO import DiscoveryPage

class sub_cancel(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\subchannel\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_cancelsub(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        channel.channelele(self.driver).click_edit_addchannel()
        mine=channel.channelele(self.driver).allindex()
        channel.channelele(self.driver).click_add_channel()
        other=nicechoice.choose(self.driver).find_allchannel(mine[1])
        print (u"先去添加一频道-%s"%other[0])
        nicechoice.choose(self.driver).click_subone(other[0])
        self.driver.back()
        try:
            self.assertTrue(self.driver.find_element_by_name(other[0]))
            self.driver.back()
            self.assertTrue(self.driver.find_element_by_name(other[0]))
            print (u"已成功添加一频道-%s"%other[0])
        except:
            print (u"添加一频道异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"添加一频道异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        else:
            channel.channelele(self.driver).click_edit_addchannel()
            channel.channelele(self.driver).click_add_channel()
            nicechoice.choose(self.driver).click_subone(other[0])
            self.driver.back()
            try:
                self.assertFalse(self.driver.find_elements_by_name(other[0]))
                self.driver.back()
                self.assertFalse(self.driver.find_elements_by_name(other[0]))
            except:
                print (u"取消订阅频道出现异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body1=u"取消订阅频道出现异常"
                smail().send_errormsg(str(filename),body1,self.work_path)

if __name__=="__main__":
    unittest.main()