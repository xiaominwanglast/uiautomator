#coding:utf-8

import sys
import time
import os
import unittest
sys.path.append (r"..")

from apptest.PO import BasePage
from apptest.PO import SearchPage
from apptest.PO import Superunit
from apptest.Public.getmethodname  import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail


class standard(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\subchannel\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_standard(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        SearchPage.Search(self.driver).click_entry()
        SearchPage.Search(self.driver).input_keywords(u"梅西")
        SearchPage.Search(self.driver).click_btn_search()
        try:
            self.assertTrue(SearchPage.Search(self.driver).find_subscribe_btn())
            self.assertTrue(SearchPage.Search(self.driver).find_topic())
        except:
            print (u"符合订阅规则,搜索界面异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"符合订阅规则,搜索界面异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        SearchPage.Search(self.driver).click_btn_search()
        SearchPage.Search(self.driver).input_keywords(u"胡锦涛")
        SearchPage.Search(self.driver).click_btn_search()
        try:
            self.assertFalse(SearchPage.Search(self.driver).find_subscribe_btns())
            self.assertTrue(SearchPage.Search(self.driver).find_topic())
        except:
            print (u"不符合订阅规则,搜索界面异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"不符合订阅规则,搜索界面异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        SearchPage.Search(self.driver).click_btn_search()
        SearchPage.Search(self.driver).input_keywords(u"黑盒测试")
        SearchPage.Search(self.driver).click_btn_search()
        try:
            self.assertFalse(SearchPage.Search(self.driver).find_subscribe_btns())
            self.assertFalse(SearchPage.Search(self.driver).find_topics())
            self.assertTrue(SearchPage.Search(self.driver).find_nums())
        except:
            print (u"无搜索结果订阅规则,搜索界面异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body1=u"无搜索结果订阅规则,搜索界面异常"
            smail().send_errormsg(str(filename),body1,self.work_path)
if __name__=="__main__":
    unittest.main()