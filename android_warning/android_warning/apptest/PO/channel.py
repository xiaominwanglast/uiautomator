#coding:utf-8
import random
from BasePage import Base
from selenium.webdriver.common.by import By
import time

class channelele(Base):

    channel_tv=(By.CLASS_NAME,"android.widget.TextView")
    news_enter=(By.ID,"%s:id/ll_news_bottom"%Base.capabilities['appPackage'])
    edit_addchannel=(By.ID,"%s:id/iv_news_arrow"%Base.capabilities['appPackage'])
    #我的频道，频道推荐，添加，编辑
    mine_channel=(By.ID,"%s:id/tv_select_tips"%Base.capabilities['appPackage'])
    suggest_channel=(By.ID,"%s:id/more_category_text"%Base.capabilities['appPackage'])
    add_channel=(By.ID,"%s:id/iv_add_subscribe"%Base.capabilities['appPackage'])
    edit_channel=(By.ID,"%s:id/tv_edit"%Base.capabilities['appPackage'])
    #返回
    channel_back=(By.ID,"%s:id/ll_widgetTitleBar_left"%Base.capabilities['appPackage'])
    #频道名字
    channel_name=(By.ID,"%s:id/text_item"%Base.capabilities['appPackage'])
    #新闻信息
    news_topic=(By.ID,"%s:id/tv_topic"%Base.capabilities['appPackage'])

    #频道
    tv=(By.ID,"%s:id/tv"%Base.capabilities['appPackage'])
    #删除按钮
    channel_delete=(By.ID,"%s:id/iv_channel_del"%Base.capabilities['appPackage'])
    backleft=(By.ID,"%s:id/tv_titleBarWidget_leftImgBtnText"%Base.capabilities['appPackage'])

    def click_backleft(self):
        self.find_element(*self.backleft).click()
        time.sleep(2)
    def find_channel_delete(self):
        return self.find_elements(*self.channel_delete)

    def find_tv(self):
        return self.find_elements(*self.tv)

    def find_news_topic(self):
        return self.find_element(*self.news_topic)

    def find_channel_name(self):
        return self.find_elements(*self.channel_name)

    def click_channel_back(self):
        self.find_element(*self.channel_back).click()
        time.sleep(3)
    #classname值查看元素
    def classname(self,i):
        return self.find_element_by_android_uiautomator("new UiSelector().className(\"android.widget.RelativeLayout\").index(%d)"%i)
    #index值查看元素
    def index(self,i):
        return self.find_elements_by_android_uiautomator("new UiSelector().resourceId(\"%s:id/rl_subscribe\").index(%d)"%(Base.capabilities['appPackage'],i))

    def indexone(self,i):
        return self.find_element_by_android_uiautomator("new UiSelector().resourceId(\"%s:id/rl_subscribe\").index(%d)"%(Base.capabilities['appPackage'],i))

    def click_indexone(self,i):
        self.find_element_by_android_uiautomator("new UiSelector().resourceId(\"%s:id/rl_subscribe\").index(%d)"%(Base.capabilities['appPackage'],i)).click()
        time.sleep(1)

    def find_mine_channel(self):
        return self.find_element(*self.mine_channel)

    def find_suggest_channel(self):
        return self.find_element(*self.suggest_channel)

    def click_add_channel(self):
        self.find_element(*self.add_channel).click()
        time.sleep(2)

    def click_edit_channel(self):
        self.find_element(*self.edit_channel).click()
        time.sleep(2)

    def click_edit_addchannel(self):
        self.find_element(*self.edit_addchannel).click()
        time.sleep(2)

    def find_channel_tv(self):
        return self.find_elements(*self.channel_tv)


    def find_news_enter(self):
        self.find_element(*self.news_enter)
        time.sleep(2)

    def click_news_enter(self):
        self.find_element(*self.news_enter).click()
        time.sleep(2)

#返回选中的频道
    def select_channel(self):
        e=self.find_elements(*self.tv)
        for i in e:
            if(i.is_selected()):
                select=i.text
                return select

#依次返回 我的频道数量，我的频道列表，推荐频道数量，推荐频道列表
    def allindex(self):
        list1=[]
        list3=[]
        e=self.driver.find_elements_by_class_name("android.widget.TextView")
        for i in e:
            list1.append(i.text)
        indexedit=list1.index(u"编辑")
        indexsuggest=list1.index(u"频道推荐")
        list2=list1[indexedit+1:indexsuggest]
        Base(self.driver).do_swipe(self.driver,"up")
        e1=self.driver.find_elements_by_class_name("android.widget.TextView")
        for i in e1:
            list3.append(i.text)
        indexsuggests=list3.index(u"频道推荐")
        list4=list3[indexsuggests+1:]
        Base(self.driver).do_swipe(self.driver,"down")
        return len(list2),list2,len(list4),list4


#依次返回 垂直频道列表，自定义频道列表，第一位自定义频道的位置
    def allchannel(self,listmine):
        newlist=[]
        otherlist=[]
        index=''
        listX=[u"头条",u"时尚",u"笑话",u"人文",u"星座",u"科技","CBA",u"国内",u"社会",u"上海",u"国际",u"健康",u"娱乐",
               u"军事",u"暖文",u"体育",u"财经",u"游戏",u"汽车",u"科学",u"互联网",u"数码",u"保健",u"健身",u"饮食",u"减肥",
               "NBA",u"德甲",u"意甲",u"网球",u"中超",u"西甲",u"英超",u"棋牌",u"高尔夫",u"排球",u"羽毛球",u"家居",u"外汇",
               u"保险",u"不动产",u"黄金",u"新三板",u"股票",u"期货",u"基金",u"理财",u"电影",u"电视",u"八卦"]
        for i in listmine:
            if(i in listX):
                newlist.append(i)
        if u"头条" in newlist:
            newlist.remove(u"头条")
        for i in listmine:
            if(i not in listX):
                otherlist.append(i)
                index=listmine.index(otherlist[0])
        return newlist,otherlist,index

#返回当前界面频道推荐之后的所有频道(只限于当前不做滑动)
    def sugggestfirst(self):
        list=[]
        e=self.driver.find_elements_by_class_name("android.widget.TextView")
        for i in e:
            list.append(i.text)
        indexsuggest=list.index(u"频道推荐")
        listsu=list[indexsuggest+1:]
        return list[indexsuggest+1],listsu

