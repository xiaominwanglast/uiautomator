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
class drawmoney_zhifubao(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_zhifubao(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        MinePage.Mine(self.driver).click_purse()
        PursePage.purse(self.driver).click_drawmoney()
        self.driver.back()
        time.sleep(2)
        try:
            PursePage.purse(self.driver).click_drawmoney()
        except:
            pass
        try:
            self.assertTrue(PursePage.purse(self.driver).find_zhifubaotext())
        except:
            self.driver.back()
            PursePage.purse(self.driver).click_drawmoney()
        else:
            try:
                self.assertTrue(PursePage.purse(self.driver).find_zhifubaotext())
            except:
                print (u"钱包>提现界面-出现异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"钱包>提现界面-出现异常"
                smail().send_errormsg(str(filename),body,self.work_path)
            self.driver.back()
            self.driver.back()


