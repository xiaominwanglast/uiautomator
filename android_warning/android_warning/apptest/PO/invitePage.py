#coding:utf-8
from BasePage import Base
from selenium.webdriver.common.by import  By
import time

class Invite(Base):
    my_code=(By.ID,"%s:id/tv_my_code"%Base.capabilities['appPackage'])
    fs_reward=(By.ID,"%s:id/tv_friends_rewards"%Base.capabilities['appPackage'])
    fs_flow=(By.ID,"%s:id/tv_friends_flow"%Base.capabilities['appPackage'])
    invite_rule=(By.NAME,u"邀请规则")
    qqspace=(By.NAME,u"QQ空间")
    qqcommit=(By.NAME,u"发表")

    def click_qqcommit(self):
        self.find_element(*self.qqcommit).click()
        time.sleep(4)
    def click_qqspace(self):
        self.find_element(*self.qqspace).click()
        time.sleep(5)
    def click_inviterule(self):
        self.find_element(*self.invite_rule).click()
        time.sleep(2)
    def find_mycode(self):
        return self.find_element(*self.my_code)
    def find_fsreward(self):
        return self.find_element(*self.fs_reward)
    def click_fsreward(self):
        self.find_element(*self.fs_reward).click()
        time.sleep(1)

    def find_fsflow(self):
        return self.find_element(*self.fs_flow)
    def click_fsflow(self):
        self.find_element(*self.fs_flow).click()
        time.sleep(6)