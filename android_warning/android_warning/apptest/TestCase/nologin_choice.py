#coding:utf-8
import random
import sys
import time
import os
import unittest
sys.path.append (r"..")
from random import choice

from apptest.PO import Superunit,MinePage
from apptest.Public.getmethodname  import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.PO import DiscoveryPage
from apptest.PO import nicechoice
#精选>UI>未登录
#1.发现>精选，检查精选首页
#2.选择任意一级二级导航，比如科技，健康，社会，国内等

class nologin_choice(Superunit.initunit):
    work_path=os.getcwd()+"\\screen\\nologin\\choice\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    body1=u"发现>精选>UI>未登录>UI检查-空白页"
    def test_01_choice(self):
        u"""发现精选UI测试"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        DiscoveryPage.Discovery(self.driver).click_foundentry()
        nicechoice.choose(self.driver).click_choice()
        try:
            self.assertTrue(nicechoice.choose(self.driver).find_category())
            self.assertTrue(nicechoice.choose(self.driver).find_texttitle())
        except:
            print (u"精选>UI>UI检查-空白页")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body1)
if __name__=="__main__":
    unittest.main()
