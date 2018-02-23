#coding:utf-8
import time
import unittest

from apptest.PO import Superunit
from apptest.PO import  BasePage
from apptest.PO import LoginPage
from apptest.PO import MinePage
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.Public.getmethodname import GetName
import os





class AppLoginTest(Superunit.initunit):
    u"""测试登录接口"""
    work_path=os.path.dirname(os.getcwd())+"\\screen\\login\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    #QQ号进行登录操作
    def  test_01_login_QQ (self):
        u"""QQ号进行登录"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        LoginPage.Login(self.driver).dologout()
        self.driver.find_element_by_id("%s:id/tv_qq"%self.app).click()
        time.sleep(4)
        print ("查看QQ登录入口".decode("utf-8"))
        try:
            BasePage.Base(self.driver).tapxy(0.5,0.8,self.driver,6)
        except:
            print ("点击不成功".decode("utf-8"))
        try:
            self.assertTrue(MinePage.Mine(self.driver).find_logintip())
        except:
            print (u"QQ登陆异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"QQ登陆异常"
            smail().send_errormsg(str(filename),body,self.work_path)

    def test_03_login_weixin(self):
        u"""微信号进行登录"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        LoginPage.Login(self.driver).dologout()
        self.driver.find_element_by_id("%s:id/tv_wechat"%self.app).click()
        time.sleep(4)
        try:
            BasePage.Base(self.driver).tapxy(0.5,0.7,self.driver,5)
        except:
            print (u"weixin登陆异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"weixin登陆异常"
            smail().send_errormsg(str(filename),body,self.work_path)

    def test_02_login_weibo(self):
        u"""微博号进行登录"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        LoginPage.Login(self.driver).dologout()
        self.driver.find_element_by_id("%s:id/tv_sina"%self.app).click()
        time.sleep(6)
        try:
            self.assertTrue(MinePage.Mine(self.driver).find_logintip())
        except:
            print (u"weibo登陆异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"weibo登陆异常"
            smail().send_errormsg(str(filename),body,self.work_path)



if __name__=="__main__":
    testunit=unittest.TestSuite()
    testunit.addTest( unittest.defaultTestLoader.loadTestsFromTestCase(AppLoginTest))



