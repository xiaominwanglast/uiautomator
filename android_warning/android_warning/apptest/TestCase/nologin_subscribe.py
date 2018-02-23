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

class nologin_subscribe(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\search\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_delhistroy(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        SearchPage.Search(self.driver).click_entry()
        print (u"需要分别添加7个搜索词，分别为--a,b,c,d,f,g,h,h")
        list=["a","b","c","d","f","g","h","h"]
        for i in list:
            SearchPage.Search(self.driver).input_keywords(i)
            SearchPage.Search(self.driver).click_btn_search()
            SearchPage.Search(self.driver).click_btn_search()
        BasePage.Base(self.driver).do_swipe(self.driver,"up")
        try:
            self.assertTrue(self.driver.find_element_by_name(u"搜索记录"))
            self.assertTrue(SearchPage.Search(self.driver).find_clearhistory())
            historylist=SearchPage.Search(self.driver).find_counthistory()
            self.assertEqual(historylist[0],7)
            self.assertEqual(historylist[1],list[1:7])
        except:
            print (u"搜索记录条数显示异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"搜索记录条数显示异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        else:
            e=SearchPage.Search(self.driver).find_tvhistory()
            e[1].click()
            time.sleep(3)
            try:
                self.assertTrue(SearchPage.Search(self.driver).find_topic())
                self.assertTrue(SearchPage.Search(self.driver).find_btn_search())
            except:
                print (u"点击第一条记录后进入订阅界面显示异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body1=u"点击第一条记录后进入订阅界面显示异常"
                smail().send_errormsg(str(filename),body1,self.work_path)
            else:
                SearchPage.Search(self.driver).click_btn_search()
                SearchPage.Search(self.driver).click_ivhistory()
                e1=SearchPage.Search(self.driver).find_tvhistory()
                try:
                    self.assertNotEqual(e1[1].text,list[-2:-1][0])
                except:
                    print (u"删除第一条搜索记录后仍然存在记录异常")
                    filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                    body2=u"删除第一条搜索记录后仍然存在记录异常"
                    smail().send_errormsg(str(filename),body2,self.work_path)
                else:
                    BasePage.Base(self.driver).do_swipe(self.driver,"up")
                    SearchPage.Search(self.driver).click_clearhistory()
                    try:
                        self.assertFalse(self.driver.find_elements_by_name(u"搜索记录"))
                        self.assertFalse(SearchPage.Search(self.driver).find_tvhistory())
                    except:
                        print (u"清除所有记录后仍然存在记录异常")
                        filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                        body2=u"清除所有记录后仍然存在记录异常"
                        smail().send_errormsg(str(filename),body2,self.work_path)

if __name__=="__main__":
    unittest.main()