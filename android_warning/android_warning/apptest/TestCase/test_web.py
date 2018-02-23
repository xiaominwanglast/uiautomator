#coding:utf-8

import unittest
import time,os
from apptest.PO import Superunit
from apptest.Public import connect
from apptest.PO import MinePage
from apptest.PO import LoginPage
class webstate(Superunit.initunit):
    def test_01_checkweb(self):
        MinePage.Mine(self.driver).click_mine_entry()
        print (u"检查网络状态")
        if connect.webstate(self.driver) != "WIFI_ONLY":
            connect.connect_onlywifi(self.driver)
        else:
            print (u"此时网络wifi已经打开")
        time.sleep(3)
        LoginPage.Login(self.driver).dologout()
        if connect.webstate(self.driver) != "WIFI_ONLY":
            kill_appium()

def kill_appium():
    p = os.popen('netstat -ano|findstr 4723|findstr LISTENING')
    out = p.read()
    print out
    pid = out.split()[-1]
    print pid
    os.popen('taskkill /pid %s /f'%pid)
if __name__=="__main__":
    unittest.main()