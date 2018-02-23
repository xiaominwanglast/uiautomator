#coding:utf-8
from BasePage import Base
from Superunit import initunit
import  random

from selenium.webdriver.common.by import  By
import time


class Search(Base):
    search_entry_loc = (By.ID,"%s:id/rb_bottom_search"%Base.capabilities['appPackage'])
    clearHistory_loc  = (By.ID,"%s:id/tv_clearHistory"%Base.capabilities['appPackage'])
    tvhistory=(By.ID,"%s:id/tv_history"%Base.capabilities['appPackage'])
    ivhistory=(By.ID,"%s:id/iv_history"%Base.capabilities['appPackage'])

    text_hotwords_loc = (By.ID,"%s:id/text_hotwords"%Base.capabilities['appPackage'])
    btn_search_loc =  (By.ID,"%s:id/btn_search"%Base.capabilities['appPackage'])
    edit_search_loc = (By.ID,"%s:id/edit_search"%Base.capabilities['appPackage'])
    btn_clear_loc =  (By.ID,"%s:id/btn_clear"%Base.capabilities['appPackage'])
    tv_topic_loc = (By.ID,"%s:id/tv_topic"%Base.capabilities['appPackage'])
    tv_time=(By.ID,"%s:id/tv_time"%Base.capabilities['appPackage'])
    subscribe_btn=(By.ID,"%s:id/btn_subscribe"%Base.capabilities['appPackage'])
    subscribe_back=(By.ID,"%s:id/ll_widgetTitleBar_left"%Base.capabilities['appPackage'])

    def click_ivhistory(self):
        self.find_element(*self.ivhistory).click()
        time.sleep(2)

    def find_tvhistory(self):
        return self.find_elements(*self.tvhistory)
    def find_clearhistory(self):
        return self.find_element(*self.clearHistory_loc)
    def click_clearhistory(self):
        self.find_element(*self.clearHistory_loc).click()
#订阅界面返回
    def click_subscribe_back(self):
        self.find_element(*self.subscribe_back).click()
        time.sleep(2)
#订阅
    def click_subscribe_btn(self):
        self.find_element(*self.subscribe_btn).click()
        time.sleep(3)
    def find_subscribe_btn(self):
        return self.find_element(*self.subscribe_btn)
    def find_subscribe_btns(self):
        return self.find_elements(*self.subscribe_btn)
#进入到搜索入口
    def  click_entry(self):
        self.find_element(*self.search_entry_loc).click()
        time.sleep(2)
    def find_tvtime(self):
        return self.find_elements(*self.tv_time)

#输入关键字
    def input_keywords (self,keywords):
        self.find_element(*self.edit_search_loc).send_keys(keywords)
        time.sleep(1)

#点击搜索框后面的搜索按钮
    def click_btn_search(self):
        self.find_element(*self.btn_search_loc).click()
        time.sleep(1)
    def find_btn_search(self):
        return self.find_element(*self.btn_search_loc)

#随机点击点击热门搜索下的关键词
    def click_text_hotwords(self,num):
        self.find_elements(*self.text_hotwords_loc)[random.randint(0,num)].click()
        time.sleep(6)


    def find_nums(self):
       return self.find_elements(*self.text_hotwords_loc)


    def find_topic(self):
        return  self.find_element(*self.tv_topic_loc)
    def find_topics(self):
        return  self.find_elements(*self.tv_topic_loc)
    def find_counthistory(self):
        history=[]
        e=Search(self.driver).find_tvhistory()
        for i in e:
            history.append(i.text)
        new=history[1:]
        new.sort()
        return len(history),new