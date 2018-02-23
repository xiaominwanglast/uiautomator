#coding:utf-8
from BasePage import Base



from selenium.webdriver.common.by import  By
import time

class Login(Base):

    close_loc = (By.ID,"%s:id/iv_close"%Base.capabilities['appPackage'])
    mine_loc =(By.ID,"%s:id/rb_bottom_mine"%Base.capabilities['appPackage'])
    set_loc = (By.ID,"%s:id/iv_setting"%Base.capabilities['appPackage'])
    nologin_loc =(By.ID,"%s:id/layout_sj"%Base.capabilities['appPackage'])
    username_loc = (By.ID,"%s:id/et_tel"%Base.capabilities['appPackage'])
    password_loc= (By.ID,"%s:id/et_password"%Base.capabilities['appPackage'])
    submit_loc =(By.ID,'%s:id/tv_login'%Base.capabilities['appPackage'])
    exit_loc = (By.ID,'%s:id/btn_exit_login'%Base.capabilities['appPackage'])
    back_loc = (By.ID,'%s:id/ll_widgetTitleBar_left'%Base.capabilities['appPackage'])
    quick_login=(By.ID,"%s:id/tv_quick_login"%Base.capabilities['appPackage'])
    get_code=(By.ID,"%s:id/tv_get_code"%Base.capabilities['appPackage'])
    text_right=(By.ID,"%s:id/text_right"%Base.capabilities['appPackage'])
    #个人中心信息
    tv_command=(By.ID,"%s:id/tv_comment"%Base.capabilities['appPackage'])
    tv_title=(By.ID,"%s:id/tv_comment_title"%Base.capabilities['appPackage'])
    tv_time=(By.ID,"%s:id/tv_comment_time"%Base.capabilities['appPackage'])
    praise=(By.ID,"%s:id/ll_click_praise"%Base.capabilities['appPackage'])
    praise_number=(By.ID,"%s:id/tv_praise_number"%Base.capabilities['appPackage'])
    ii_command=(By.ID,"%s:id/ll_click_comment"%Base.capabilities['appPackage'])
    ed_command=(By.ID,"%s:id/et_comment"%Base.capabilities['appPackage'])
    iv_post=(By.ID,"%s:id/tv_post"%Base.capabilities['appPackage'])
    tv_loginqq=(By.ID,"%s:id/tv_qq"%Base.capabilities['appPackage'])

    def click_loginqq(self):
        self.find_element(*self.tv_loginqq).click()
        time.sleep(5)

    def input_iicommand(self,keywords):
        self.find_element(*self.ii_command).click()
        time.sleep(1)
        self.find_element(*self.ed_command).send_keys(keywords)
        time.sleep(1)
        self.find_element(*self.iv_post).click()
    def click_exit(self):
        self.find_element(*self.exit_loc).click()
        time.sleep(1)

    def find_praisenum(self):
        return self.find_element(*self.praise_number)
    def click_praise(self):
        self.find_element(*self.praise).click()
        time.sleep(1)
    def find_tvcommand(self):
        return self.find_elements(*self.tv_command)
    def click_tvcomand(self):
        self.find_element(*self.tv_command).click()
        time.sleep(1)
    def find_tvtitle(self):
        return self.find_elements(*self.tv_title)
    def click_tvtile(self):
        self.find_element(*self.tv_title).click()
        time.sleep(3)
    def find_tvtime(self):
        return self.find_elements(*self.tv_time)

    def find_getcode(self):
        return self.find_element(*self.get_code)
    def click_quicklogin(self):
        self.find_element(*self.quick_login).click()
        time.sleep(1)
    def input_mine(self):
        self.find_element(*self.mine_loc).click()
#        self.find_element(self.mine_loc).click()
        time.sleep(2)

    def input_nologin(self):
        self.find_element(*self.nologin_loc).click()
        time.sleep(2)
    def find_nologin(self):
        return self.find_element(*self.nologin_loc)

    def input_username(self,username):

        self.find_element(*self.username_loc).send_keys(username)
        time.sleep(2)

    def input_password(self,passwrod):
        self.find_element(*self.password_loc).send_keys(passwrod)
        time.sleep(2)

    def click_submit(self):
        self.find_element(*self.submit_loc).click()
        time.sleep(5)

    def find_submit(self):
        return self.find_element(*self.submit_loc)

    def click_textright(self):
        self.find_element(*self.text_right).click()
        time.sleep(2)

    def dologout(self):
        self.find_element(*self.mine_loc).click()
        time.sleep(2)
        self.find_element(*self.set_loc).click()
        time.sleep(2)
        self.find_element(*self.exit_loc).click()
        time.sleep(2)
        try:
            self.find_element(*self.text_right).click()
            time.sleep(1)
        except:
            pass
        try:
            self.find_element(*self.back_loc).click()
            time.sleep(2)
        except:
            pass






