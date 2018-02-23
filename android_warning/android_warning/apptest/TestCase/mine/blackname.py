#coding:utf-8


from apptest.PO import Superunit
from apptest.PO import  MinePage
from apptest.Public.getmethodname import GetName
from apptest.PO import  NewsPage
from apptest.PO import  InsideNewsPage
from apptest.PO import LoginPage
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
import os ,time
import unittest

class blackname(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\blackname\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_black(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        LoginPage.Login(self.driver).input_mine()
        LoginPage.Login(self.driver).input_nologin()
        try:
            self.assertTrue(LoginPage.Login(self.driver).find_getcode())
            LoginPage.Login(self.driver).click_quicklogin()
        except:
            pass
        LoginPage.Login(self.driver).input_username("15015993611")
        LoginPage.Login(self.driver).input_password("123456")
        LoginPage.Login(self.driver). click_submit()
        try:
            self.assertTrue(MinePage.Mine(self.driver).find_set())
            print u"黑名单可以登陆账号-出现异常"
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"黑名单可以登陆账号-出现异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        except:
            pass

if __name__=="__main__":
    unittest.main()