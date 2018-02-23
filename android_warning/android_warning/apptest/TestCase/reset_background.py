#coding:utf-8

import unittest
import os,time
from apptest.PO import Superunit
from apptest.PO import MinePage
from apptest.PO import LoginPage
from apptest.PO import BasePage
class reset(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    def test_01_reset(self):
        u"""退出登陆，恢复测试环境"""
        LoginPage.Login(self.driver).dologout()
        a=time.strftime("%Y-%m-%d",time.localtime(time.time())).split('-')[2]
        if int(a)%2==0:
            BasePage.Base(self.driver).do_swipe(self.driver,"up")
            time.sleep(5)
            MinePage.Mine(self.driver).click_night()
        time.sleep(5)
if __name__=="__main__":
    unittest.main()
