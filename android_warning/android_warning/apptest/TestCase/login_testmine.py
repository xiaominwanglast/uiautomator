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

class login_mine(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\login\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    def test_01_mine(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        try:
            self.assertTrue(CollectPage.Collect(self.driver).find_mine_collect())
            self.assertTrue(MinePage.Mine(self.driver).find_set())
            self.assertTrue(MinePage.Mine(self.driver).find_purse())
            self.assertTrue(MinePage.Mine(self.driver).find_mall())
            self.assertTrue(MinePage.Mine(self.driver).find_despoil())
            self.assertTrue(MinePage.Mine(self.driver).find_msg())
            self.assertTrue(MinePage.Mine(self.driver).find_invite())
            BasePage.Base(self.driver).do_swipe(self.driver,"up")
            self.assertTrue(MinePage.Mine(self.driver).find_hisred())
            self.assertTrue(MinePage.Mine(self.driver).find_task())
            self.assertTrue(MinePage.Mine(self.driver).find_offline())
            self.assertTrue(MinePage.Mine(self.driver).find_night())
            self.assertTrue(MinePage.Mine(self.driver).find_feedback())
            BasePage.Base(self.driver).do_swipe(self.driver,"down")
        except:
            print (u"我的界面显示异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"我的界面显示异常"
            smail().send_errormsg(str(filename),body,self.work_path)