#coding:utf-8

import sys
import time
import os

sys.path.append (r"..")

from apptest.PO import BasePage
from apptest.PO import MinePage
from apptest.PO import Superunit
from apptest.PO import CollectPage
from apptest.Public.getmethodname  import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
import unittest
class nologin_mine(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    body1=u"我的>UI>未登录>UI检查-空白页"
    def test_01_mine(self):
        u"""我的界面UI测试"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        try:
            self.assertTrue(MinePage.Mine(self.driver).find_set())
            self.assertTrue(MinePage.Mine(self.driver).find_mall())
      #      self.assertTrue(MinePage.Mine(self.driver).find_despoil())
            BasePage.Base(self.driver).do_swipe(self.driver,"up")
            self.assertTrue(MinePage.Mine(self.driver).find_feedback())
            BasePage.Base(self.driver).do_swipe(self.driver,"down")
        except:
            print (u"我的>UI>UI检查-空白页")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body1)


if __name__=="__main__":
    unittest.main()