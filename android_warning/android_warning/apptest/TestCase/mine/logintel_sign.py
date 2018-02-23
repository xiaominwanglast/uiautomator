#coding:utf-8


from apptest.PO import Superunit
from apptest.PO import  MinePage
from apptest.Public.getmethodname import GetName
from apptest.PO import  NewsPage
from apptest.PO import  InsideNewsPage
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
import os ,time
from apptest.PO import  TaskCenterPage
from apptest.PO import  PursePage
from apptest.PO import LoginPage
import unittest
from apptest.Public import connect
class tel_signed(Superunit.initunit):

    work_path=os.path.dirname(os.getcwd())+"\\screen\\sign\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_checksign(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        try:
            self.assertTrue(NewsPage.News(self.driver).find_sign())
            print (u"账号未签到")
        except:
            print (u"账号已签到")
        else:
            connect.connect_noconnect(self.driver)
            NewsPage.News(self.driver).click_sign()
            try:
                self.assertTrue(NewsPage.News(self.driver).find_sign())
            except:
                print (u"网络异常时新闻页签到显示异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body1=u"网络异常时新闻页签到显示异常"
                smail().send_errormsg(str(filename),body1,self.work_path)
            else:
                connect.connect_onlywifi(self.driver)
                MinePage.Mine(self.driver).click_mine_entry()
                NewsPage.News(self.driver).click_news_entry()
                NewsPage.News(self.driver).click_sign()
                MinePage.Mine(self.driver).click_mine_entry()
                MinePage.Mine(self.driver).click_task()
                try:
                    e=TaskCenterPage.taskcenter(self.driver).find_signtoday_el()
                    self.assertEqual(e[0],"+")
                except:
                    print (u"新闻页签到-任务中心查看显示异常")
                    filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                    body1=u"新闻页签到-任务中心查看显示异常"
                    smail().send_errormsg(str(filename),body1,self.work_path)
    def test_02_checkweb(self):
        MinePage.Mine(self.driver).click_mine_entry()
        print (u"检查网络状态")
        if connect.webstate(self.driver) != "WIFI_ONLY":
            connect.connect_onlywifi(self.driver)
        else:
            print (u"此时网络wifi已经打开")

if __name__=="__main__":
    unittest.main()






















