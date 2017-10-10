#coding:utf-8
from BasePage import Base
from appium import webdriver

from selenium.webdriver.common.by import  By
import time

class Closement (Base):
    mine_loc =(By.ID,"%s:id/rb_bottom_mine"%Base.capabilities['appPackage'])
    set_loc = (By.ID,"%s:id/rl_setting"%Base.capabilities['appPackage'])
    movement_loc = (By.ID,"%s:id/rl_notify_toggle"%Base.capabilities['appPackage'])

    ok_loc = (By.ID,"%s:id/download_clear_ok"%Base.capabilities['appPackage'])

    back_loc = (By.ID,"%s:id/top_back"%Base.capabilities['appPackage'])


    '''
    def click_mine(self):

        self.find_element(*self.mine_loc).click()
        time.sleep(2)


#        self.do_swipe(self.driver,"up")

    def click_set(self):
        self.find_element(*self.set_loc).click()
        time.sleep(2)

    def click_movement(self):
        self.find_element(*self.movement_loc).click()
        time.sleep(2)

    def click_ok(self):
        self.find_element(*self.ok_loc).click()
        time.sleep(2)

    def click_back(self):
        self.find_element(*self.back_loc).click()
        time.sleep(2)
    '''

    def do_close(self):
        self.find_element(*self.mine_loc).click()
        time.sleep(2)

        self.do_swipe(self.driver,"up")

        self.find_element(*self.set_loc).click()
        time.sleep(2)

        self.find_element(*self.movement_loc).click()
        time.sleep(2)

        self.find_element(*self.ok_loc).click()
        time.sleep(2)

        self.find_element(*self.back_loc).click()
        time.sleep(2)


