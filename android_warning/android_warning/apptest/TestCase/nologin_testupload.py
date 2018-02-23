#coding:utf-8
import random
import sys
import time
import os
import unittest
sys.path.append (r"..")

from apptest.PO import Superunit
from apptest.Public.getmethodname  import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.PO import NewsPage
from apptest.PO import BasePage

#新闻信息流>上拉加载
#1.新闻>信息流页面做上拉滑动
class nologin_drageupload(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\news\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_drageup(self):
        name1=self.__class__.__name__ +'.'+GetName.get_current_function_name()
        for i in range(1,10):
            before=NewsPage.News(self.driver).find_topic().get_attribute('name')
            BasePage.Base(self.driver).do_swipe(self.driver,"up")
            if (i < 6):
                continue
            next=NewsPage.News(self.driver).find_topic().get_attribute('name')
            try:
                self.assertNotEqual(before,next)
            except:
                print (u"信息上拉加载出现异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"信息上拉加载出现异常"
                smail().send_errormsg(str(filename),body,self.work_path)

if __name__=="__main__":
    unittest.main()

