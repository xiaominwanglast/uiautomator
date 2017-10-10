#coding:utf-8
from BasePage import Base
from appium import  webdriver


from selenium.webdriver.common.by import  By
import time

class Login(Base):

    mine_loc =(By.ID,"%s:id/rb_bottom_mine"%Base.capabilities['appPackage'])
    set_loc = (By.ID,"%s:id/rl_setting"%Base.capabilities['appPackage'])
    nologin_loc =(By.ID,"%s:id/iv_usr_image"%Base.capabilities['appPackage'])
    username_loc = (By.ID,"%s:id/edit_accountname"%Base.capabilities['appPackage'])
    password_loc= (By.ID,"%s:id/edit_password"%Base.capabilities['appPackage'])
    submit_loc =(By.ID,'%s:id/btn_login'%Base.capabilities['appPackage'])
    exit_loc = (By.ID,'%s:id/btn_exit_login'%Base.capabilities['appPackage'])
    back_loc = (By.ID,'%s:id/top_back'%Base.capabilities['appPackage'])

    def input_mine(self):
        self.find_element(*self.mine_loc).click()
#        self.find_element(self.mine_loc).click()
        time.sleep(2)

    def input_nologin(self):
        self.find_element(*self.nologin_loc).click()
        time.sleep(2)

    def input_username(self,username):

        self.find_element(*self.username_loc).send_keys(username)
        time.sleep(2)

    def input_password(self,passwrod):
        self.find_element(*self.password_loc).send_keys(passwrod)
        time.sleep(2)

    def click_submit(self):
        self.find_element(*self.submit_loc).click()


    def dologout(self):
        self.find_element(*self.mine_loc).click()
        time.sleep(2)

        self.do_swipe(self.driver,"up")

        self.find_element(*self.set_loc).click()
        time.sleep(2)

        self.find_element(*self.exit_loc).click()
        time.sleep(2)

        self.do_swipe(self.driver,"down")
        try:
            self.find_element(*self.back_loc).click()
            time.sleep(2)
        except:
            print (u"不用返回")









