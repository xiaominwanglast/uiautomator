#coding:utf-8
from BasePage import Base
from selenium.webdriver.common.by import  By
import time

class choose(Base):
    tvsearch=(By.ID,"%s:id/tv_search"%Base.capabilities['appPackage'])
    category=(By.ID,"%s:id/tv_catagory"%Base.capabilities['appPackage'])
    texttitle=(By.ID,"%s:id/text_title"%Base.capabilities['appPackage'])
    textsub=(By.ID,"%s:id/text_sub"%Base.capabilities['appPackage'])
    textdetail=(By.ID,"%s:id/text_detail"%Base.capabilities['appPackage'])
#    choice=(By.ID,"%s:id/rb_subscribt"%Base.capabilities['appPackage'])
    choice=(By.NAME,u"精选")
    subscribe=(By.ID,"%s:id/tv_titleBarWidget_rightBtn"%Base.capabilities['appPackage'])
    subscribe_back=(By.ID,"%s:id/ll_widgetTitleBar_left"%Base.capabilities['appPackage'])
    layoutsearch=(By.ID,"%s:id/layout_search"%Base.capabilities['appPackage'])

    def click_layoutsearch(self):
        self.find_element(*self.layoutsearch).click()
        time.sleep(2)
    def click_back(self):
        self.find_element(*self.subscribe_back).click()
        time.sleep(2)
    def click_subscribe(self):
        self.find_element(*self.subscribe).click()
        time.sleep(2)
    def click_choice(self):
        self.find_element(*self.choice).click()
        time.sleep(2)
    def find_texttitle(self):
        return self.find_elements(*self.texttitle)
    def find_textone(self):
        return self.find_element(*self.texttitle)
    def find_category(self):
        return self.find_elements(*self.category)
    def find_tvsearch(self):
        return self.find_element(*self.tvsearch)
    def find_textsub(self):
        return self.find_elements(*self.textsub)
    def click_textsub(self):
        self.find_element(*self.textsub).click()
    def find_textdetail(self):
        return self.find_elements(*self.textdetail)
    #提取不在我的频道的当前界面里的频道
    def find_allchannel(self,mine):
        add=[]
        e=choose(self.driver).find_texttitle()
        for i in e:
            if (i.text not in mine):
                add.append(i.text)
        return add
    #通过当前频道位置，点击后面订阅，并且返回订阅数量
    def click_sub(self,mine):
        add=[]
        j=0
        e=choose(self.driver).find_texttitle()
        b=choose(self.driver).find_textsub()
        for i in e:
            add.append(i.text)
            if (i.text not in mine):
                index=add.index(i.text)
                b[index].click()
                j=j+1
        return j
    #通过某一个频道去点击后面订阅
    def click_subone(self,one):
        add=[]
        e=choose(self.driver).find_texttitle()
        b=choose(self.driver).find_textsub()
        for i in e:
            add.append(i.text)
        b[add.index(one)].click()