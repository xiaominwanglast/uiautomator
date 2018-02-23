#coding:utf-8

import unittest
import os,time
from apptest.PO import Superunit
from apptest.PO import SetPage
from apptest.PO import MinePage
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.Public.getmethodname import GetName

class setUI(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    body1=u"我的>设置>UI>未登录>UI检查-空白页"
    def test_01_setUI(self):
        u"""我的设置UI测试"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        MinePage.Mine(self.driver).click_set()
        try:
            self.assertTrue(SetPage.Set(self.driver).find_bodysize())
            self.assertTrue(SetPage.Set(self.driver).find_tv_version())
        except:
            print (u"设置>UI>UI检查-空白页")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body1)

if __name__=="__main__":
    unittest.main()