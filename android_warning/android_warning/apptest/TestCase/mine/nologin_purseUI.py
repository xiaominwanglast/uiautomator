#coding:utf-8
from apptest.PO import Superunit
from apptest.PO import MinePage
from apptest.Public.getmethodname import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
import os ,time
from apptest.PO import LoginPage

class nologin_purse(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    body1=u"我的>钱包>UI>未登录>检查UI-空白页"
    def test_01_UI(self):
        u"""我的钱包UI检查测试"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        MinePage.Mine(self.driver).click_purse()
        try:
            self.assertTrue(LoginPage.Login(self.driver).find_submit())
        except:
            print (u"钱包>UI>检查UI-空白页")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body1)

