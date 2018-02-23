#coding:utf-8

import sys
import time
import os

sys.path.append (r"..")


from apptest.PO import SearchPage
from apptest.PO import Superunit
from apptest.Public.getmethodname  import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail

class nologin_serach(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\search\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    body1=u"搜索>悬窗搜索>UI>未登录>UI检查-空白页"
    body2=u"悬窗搜索>搜索输入内容>UI检查-空白页"
    def test_01_search(self):
        u"""悬窗搜索UI测试"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        SearchPage.Search(self.driver).click_entry()
        try:
            self.assertTrue(SearchPage.Search(self.driver).find_nums())
            self.assertTrue(len(SearchPage.Search(self.driver).find_nums())==8)
        except:
            print (u"悬窗搜索>UI>UI检查-空白页")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body1)

    def test_02_searchinput(self):
        u"""输入搜索内容测试"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        SearchPage.Search(self.driver).click_entry()
        SearchPage.Search(self.driver).click_text_hotwords(7)
        try:
            self.assertTrue(SearchPage.Search(self.driver).find_topics())
        except:
            print (u"悬窗搜索>搜索输入内容>UI检查-空白页")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body2)


