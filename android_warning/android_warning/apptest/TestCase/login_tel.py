#coding:utf-8
import  unittest
import  time
from appium import  webdriver
from ddt import ddt,data,unpack
import csv
import os
import sys

sys.path.append (r"..")
from apptest.Public.getmethodname  import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.PO import BasePage
from apptest.PO import LoginPage
from apptest.PO import MinePage
from apptest.Public.getmethodname import GetName
def get_csv_data(file_name):
    rows = []
    data_file = open(file_name, "rb")
    reader = csv.reader(data_file)
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows
@ddt
class login (unittest.TestCase):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\login\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    def setUp(self):
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',BasePage.Base.capabilities)
        time.sleep(8)
    def tearDown(self):
        self.driver.quit()

    strpath=(os.path.dirname(os.getcwd())+"\\data\\"+"logindata.csv")
    @data(*get_csv_data(strpath))
    @unpack

    def test_01_login(self,username,password):
        u"""随机登陆手机、QQ、微信、微博，并且随机白天、夜间模式"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        a=time.strftime("%Y-%m-%d",time.localtime(time.time())).split('-')[2]
        a=0
        #手机号登陆
        if int(a)%4==0:
            login_tel(self,self.driver,username,password)
            for i in range(3):
                try:
                    self.assertTrue(LoginPage.Login(self.driver).find_submit())
                    time.sleep(600)
                    login_tel(self,self.driver,username,password)
                except:
                    break

        #QQ号登陆
        elif int(a)%4==1:
            login_QQ(self,self.driver)
            for i in range(3):
                try:
                    self.assertTrue((MinePage.Mine(self.driver).find_logintip()).text==u"手机登录/注册")
                    time.sleep(600)
                    login_QQ(self,self.driver)
                except:
                    break
        #微信号登陆
        elif int(a)%4==2:
            login_weixin(self,self.driver)
            for i in range(3):
                try:
                    self.assertTrue((MinePage.Mine(self.driver).find_logintip()).text==u"手机登录/注册")
                    time.sleep(600)
                    login_weixin(self,self.driver)
                except:
                    break
        #微博号登陆
        else:
            login_weibo(self,self.driver)
            for i in range(3):
                try:
                    self.assertTrue((MinePage.Mine(self.driver).find_logintip()).text==u"手机登录/注册")
                    time.sleep(600)
                    login_weibo(self,self.driver)
                except:
                    break

        #日期逢双 夜间模式测试
        if int(a)%2==0:
            BasePage.Base(self.driver).do_swipe(self.driver,"up")
            time.sleep(5)
            try:
                MinePage.Mine(self.driver).click_night()
            except:
                self.driver.back()
                MinePage.Mine(self.driver).click_night()

    def test_02_trykillappium(self):
        u"""确保登陆成功，一旦上面登陆不成功断开appium"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        time.sleep(2)
        #确保登陆不成功时杀掉appium
        if (MinePage.Mine(self.driver).find_logintip()).text ==u"手机登录/注册":
            print (u"我的>手机登录-登录异常")
            body1=u"我的>手机登录-登录异常"
            filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=body1)

            kill_appium()
        time.sleep(5)


def login_tel(self,driver,username,password):
    self.driver=driver
    MinePage.Mine(self.driver).click_mine_entry()
    LoginPage.Login(self.driver).input_nologin()
    try:
        self.assertTrue(LoginPage.Login(self.driver).find_getcode())
        LoginPage.Login(self.driver).click_quicklogin()
    except:
        pass
    LoginPage.Login(self.driver).input_username(username)
    LoginPage.Login(self.driver).input_password(password)
    LoginPage.Login(self.driver).click_submit()
    time.sleep(8)

def login_QQ(self,driver):
    self.driver=driver
    MinePage.Mine(self.driver).click_mine_entry()
    self.driver.find_element_by_id("com.songheng.eastnews:id/layout_qq").click()
    time.sleep(4)
    BasePage.Base(self.driver).tapxy(0.5,0.8,self.driver,6)
    time.sleep(8)

def login_weixin(self,driver):
    self.driver=driver
    MinePage.Mine(self.driver).click_mine_entry()
    self.driver.find_element_by_id("com.songheng.eastnews:id/layout_wechat").click()
    time.sleep(4)
    BasePage.Base(self.driver).tapxy(0.5,0.7,self.driver,5)
    time.sleep(8)

def login_weibo(self,driver):
    self.driver=driver
    MinePage.Mine(self.driver).click_mine_entry()
    MinePage.Mine(self.driver).click_newlogin()
    self.driver.find_element_by_id("com.songheng.eastnews:id/tv_sina").click()
    time.sleep(8)

def kill_appium():
    p = os.popen('netstat -ano|findstr 4723|findstr LISTENING')
    out = p.read()
    print out
    pid = out.split()[-1]
    print pid
    os.popen('taskkill /pid %s /f'%pid)




if __name__ == "__main__":
    unittest.main()


