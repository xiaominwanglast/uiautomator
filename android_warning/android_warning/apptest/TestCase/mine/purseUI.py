#coding:utf-8

from apptest.PO import Superunit
from apptest.PO import MinePage
from apptest.Public.getmethodname import GetName
from apptest.PO import BasePage
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
import os ,time
from apptest.PO import LoginPage
from apptest.PO import SetPage
from apptest.PO import PursePage

class purseUI(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    body1=u"我的>钱包>UI>已登录>UI检查-空白页"
    def test_01_UI(self):
        u"""我的钱包UI检查测试"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        MinePage.Mine(self.driver).click_purse()
        time.sleep(5)
        try:
            self.assertTrue(PursePage.purse(self.driver).find_login_total_bonus())
            self.assertTrue(PursePage.purse(self.driver).find_login_total_bonus() !=u"--")
            self.assertTrue(PursePage.purse(self.driver).find_login_yesterday_bonus() !=u"--")
            self.assertTrue(PursePage.purse(self.driver).find_purse_historybonus() !=u"--")
        except:
            print (u"我的>钱包>检查UI布局-出现异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body1)


