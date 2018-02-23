#coding:utf-8
from BasePage import Base
import random

from selenium.webdriver.common.by import By
import time

class Hot(Base):

    #发现界面
    find_hot=(By.ID,"%s:id/tv_found"%Base.capabilities['appPackage'])
#    find_hotnews=(By.ID,"%s:id/rb_news_rank"%Base.capabilities['appPackage'])
    find_hotnews=(By.NAME,u"热文")
#    find_hotman=(By.ID,"%s:id/rb_user_rank"%Base.capabilities['appPackage'])
    find_hotman=(By.NAME,u"红人")
    #热文界面元素
    hotnews_hot=(By.ID,"%s:id/rb_rank_hot"%Base.capabilities['appPackage'])
    hotnews_7days=(By.ID,"%s:id/rb_rank_7days"%Base.capabilities['appPackage'])
    hotnews_rank=(By.ID,"%s:id/rb_rank_all"%Base.capabilities['appPackage'])
    #红人界面
    hotman_share=(By.ID,"%s:id/radio_share"%Base.capabilities['appPackage'])
    hotman_read=(By.ID,"%s:id/radio_read"%Base.capabilities['appPackage'])
    hotman_income=(By.ID,"%s:id/radio_income"%Base.capabilities['appPackage'])
    #内容元素
    hot_topics=(By.ID,"%s:id/tv_topic"%Base.capabilities['appPackage'])

    #没有更多
    loadmore=(By.ID,"%s:id/load_more_error_tv"%Base.capabilities['appPackage'])
    loadmorename=(By.NAME,u"没有更多热门了哦")
    textdetail=(By.ID,"%s:id/text_detail"%Base.capabilities['appPackage'])

    def find_textdetail(self):
        return self.find_elements(*self.textdetail)

    def find_loadmore(self):
        return self.find_element(*self.loadmore)

    #点击发现
    def click_find(self):
        self.find_element(*self.find_hot).click()
        time.sleep(6)

    #点击热文
    def click_find_hotnews(self):
        self.find_element(*self.find_hotnews).click()
        time.sleep(2)

    #点击红人
    def click_find_hotman(self):
        self.find_element(*self.find_hotman).click()
        time.sleep(2)

    #点击蹿红
    def click_hotnews_hot(self):
        self.find_element(*self.hotnews_hot).click()
        time.sleep(5)
    #点击七天
    def click_hotnews_7days(self):
        self.find_element(*self.hotnews_7days).click()
        time.sleep(5)

    #点击总榜
    def click_hotnews_rank(self):
        self.find_element(*self.hotnews_rank).click()
        time.sleep(5)

    #点击分享榜
    def click_hotman_share(self):
        self.find_element(*self.hotman_share).click()
        time.sleep(3)

    #点击阅读榜
    def click_hotman_read(self):
        self.find_element(*self.hotman_read).click()
        time.sleep(3)

    #点击收入榜
    def click_hotman_income(self):
        self.find_element(*self.hotman_income).click()
        time.sleep(3)

    #搜索主题
    def find_hot_topics(self):
        return self.find_element(*self.hot_topics)
