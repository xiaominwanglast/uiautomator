#coding:utf-8

import time
import shutil
import os
import sys
sys.path.append(r"..")
import unittest
from apptest.PO import BasePage
from apptest.PO import HotPage,MinePage
from apptest.PO import Superunit
from apptest.Public.getmethodname import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.PO.BasePage import Base


class nologin_Hot(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\hot\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    body1=u"发现>热文>UI>未登录>UI检查-空白页"
    body2=u"发现>红人>UI>未登录>UI检查-空白页"
    def test_01_hotnews(self):
        u"""发现热文UI测试"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        HotPage.Hot(self.driver).click_find()
        HotPage.Hot(self.driver).click_find_hotnews()
        try:
            HotPage.Hot(self.driver).click_hotnews_hot()
            self.assertTrue(HotPage.Hot(self.driver).find_hot_topics())
            HotPage.Hot(self.driver).click_hotnews_7days()
            self.assertTrue(HotPage.Hot(self.driver).find_hot_topics())
            HotPage.Hot(self.driver).click_hotnews_rank()
            self.assertTrue(HotPage.Hot(self.driver).find_hot_topics())
        except:
            print (u"热文>UI>UI检查-空白页")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body1)

    def test_02_hotman(self):
        u"""发现红人UI测试"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        HotPage.Hot(self.driver).click_find()
        HotPage.Hot(self.driver).click_find_hotman()
        HotPage.Hot(self.driver).click_hotman_share()
        try:
            HotPage.Hot(self.driver).click_hotman_share()
            self.assertTrue(HotPage.Hot(self.driver).find_textdetail())
            HotPage.Hot(self.driver).click_hotman_read()
            self.assertTrue(HotPage.Hot(self.driver).find_textdetail())
            HotPage.Hot(self.driver).click_hotman_income()
            self.assertTrue(HotPage.Hot(self.driver).find_textdetail())
        except:
            print (u"红人>UI>UI检查-空白页")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body2)


if __name__=="__main__":
    unittest.main()