#coding:utf-8
from BasePage import Base

from selenium.webdriver.common.by import  By
import time

class feed(Base):
    write_post=(By.ID,"%s:id/tv_write_post"%Base.capabilities['appPackage'])
    send_button=(By.ID,"%s:id/send_button"%Base.capabilities['appPackage'])
    iv_camera=(By.ID,"%s:id/iv_camera"%Base.capabilities["appPackage"])
    picture=(By.ID,"com.android.gallery3d:id/photo_count")
    select=(By.ID,"com.android.gallery3d:id/head_select_right")
    text_post=(By.ID,"%s:id/chatlist_text_me"%Base.capabilities['appPackage'])
    image_post=(By.ID,"%s:id/chatlist_chat_img_me"%Base.capabilities['appPackage'])
    noconnect_text=(By.NAME,u"网络开小差啦，点击屏幕刷新")
    nomal_error=(By.NAME,u"常见问题")
    kefu_text=(By.ID,"%s:id/chatlist_text_other"%Base.capabilities['appPackage'])

    def find_kefutext(self):
        return self.find_element(*self.kefu_text)

    def find_noconnect(self):
        return self.find_element(*self.noconnect_text)
    def click_camera(self):
        self.find_element(*self.iv_camera).click()
        time.sleep(3)
    def click_btn(self):
        self.find_element(*self.send_button).click()
        time.sleep(2)

    def input_post(self,keywords):
        self.find_element(*self.write_post).send_keys(keywords)
        time.sleep(2)

    def click_picture(self):
        self.find_element(*self.picture).click()
        time.sleep(2)
    def click_select(self):
        self.find_element(*self.select).click()
        time.sleep(2)

    def find_textpost(self):
        return self.find_element(*self.text_post)

    def find_imagepost(self):
        return self.find_element(*self.image_post)

    def click_nomalerror(self):
        self.find_element(*self.nomal_error).click()
        time.sleep(2)
    def find_nomalerror(self):
        return self.find_element(*self.nomal_error)