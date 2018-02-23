#coding:utf-8
from BasePage import Base

import  random

from selenium.webdriver.common.by import  By
import time

class News(Base):

    #底部的新闻按钮
    bottom_news_loc = (By.ID,"%s:id/ll_news_bottom"%Base.capabilities['appPackage'])
    tv_topic_loc = (By.ID,"%s:id/tv_topic"%Base.capabilities['appPackage'])
    textview_loc =(By.ID,"%s:id/tv"%Base.capabilities['appPackage'])
    pageview_loc = (By.CLASS_NAME,"android.view.View")
    tvsource_loc=(By.ID,"%s:id/tv_source"%Base.capabilities['appPackage'])
    tvclose_loc=(By.ID,"%s:id/iv_close"%Base.capabilities['appPackage'])
    tv_sign_loc = (By.NAME,u"签")
    footer_low=(By.ID,"%s:id/footer_hint_text"%Base.capabilities['appPackage'])
    btn_cancel=(By.ID,"%s:id/btn_cancel"%Base.capabilities['appPackage'])
    iv_close=(By.ID,"%s:id/iv_close"%Base.capabilities['appPackage'])


    #新闻内页
    comment_in=(By.ID,"%s:id/layout_comment_number"%Base.capabilities['appPackage'])
    hots_in=(By.ID,"%s:id/tv_hotnews"%Base.capabilities['appPackage'])
    tvtitle_in=(By.ID,"%s:id/tv_title"%Base.capabilities['appPackage'])
    back_in=(By.ID,"%s:id/tv_titlebar_back"%Base.capabilities['appPackage'])
    feedback_in=(By.ID,"%s:id/tv_feedback_error"%Base.capabilities['appPackage'])
    textcontent_in=(By.ID,"%s:id/text_content"%Base.capabilities['appPackage'])
    seclose_in=(By.ID,"%s:id/tv_titleBarWidget_leftSecondBtn"%Base.capabilities['appPackage'])
    editcontent_in=(By.ID,"%s:id/edit_content"%Base.capabilities['appPackage'])
    commit_in=(By.ID,"%s:id/btn_commit"%Base.capabilities['appPackage'])

    #美女新闻界面
    beauty_picture=(By.ID,"%s:id/rl_item"%Base.capabilities['appPackage'])
    kan_picture=(By.ID,"%s:id/tv_kan_times"%Base.capabilities['appPackage'])
    zan_picture=(By.ID,"%s:id/tv_zan_times"%Base.capabilities['appPackage'])
    cai_picture=(By.ID,"%s:id/tv_cai_times"%Base.capabilities['appPackage'])
    favorite_picture=(By.ID,"%s:id/iv_favorite"%Base.capabilities['appPackage'])
    share_picture=(By.ID,"%s:id/iv_share"%Base.capabilities['appPackage'])
    nums_picture=(By.ID,"%s:id/tv_picnums"%Base.capabilities['appPackage'])
    webview=(By.ID,"%s:id/webview"%Base.capabilities['appPackage'])


    #地方频道界面显示
    location_place=(By.ID,"%s:id/tv_loaction"%Base.capabilities['appPackage'])
    temperature_place=(By.ID,"%s:id/tv_temperature"%Base.capabilities['appPackage'])
    temperature_range_place=(By.ID,"%s:id/tv_temperature_range"%Base.capabilities['appPackage'])
    des_palce=(By.ID,"%s:id/tv_des"%Base.capabilities['appPackage'])
    titletext_place=(By.ID,"%s:id/tv_titleBarWidget_titelText"%Base.capabilities['appPackage'])
    reflash_place=(By.ID,"%s:id/ll_widgetTitleBar_right"%Base.capabilities['appPackage'])
    cityname_place=(By.ID,"%s:id/tv_city_name"%Base.capabilities['appPackage'])

    #视频频道界面显示
    kvideo_video=(By.ID,"%s:id/ijkVideoView"%Base.capabilities['appPackage'])
    videotitle_video=(By.ID,"%s:id/tv_video_title"%Base.capabilities['appPackage'])
    tvtitle_video=(By.ID,"%s:id/tv_title"%Base.capabilities['appPackage'])
    play_video=(By.ID,"%s:id/player_btn"%Base.capabilities['appPackage'])
    full_video=(By.ID,"%s:id/full"%Base.capabilities['appPackage'])

   # ----------------------------------------------------
    kaiping_news=(By.ID,"%s:id/close"%Base.capabilities['appPackage'])
    kaiping_back=(By.CLASS_NAME,"android.widget.ImageButton")
    def find_kaiping(self):
        return self.find_element(*self.kaiping_news)

    def click_kaipingback(self):
        self.find_element(*self.kaiping_back).click()
        time.sleep(3)
    #--------------------------------------------------

    def find_footerlow(self):
        return self.find_element(*self.footer_low)
    def find_footerlows(self):
        return self.find_elements(*self.footer_low)

    def click_full(self):
        self.find_element(*self.full_video).click()
        time.sleep(3)
    def find_sign(self):
        return self.find_element(*self.tv_sign_loc)
    def find_signs(self):
        return self.find_elements(*self.tv_sign_loc)

    def click_sign(self):
        self.find_element(*self.tv_sign_loc).click()
        time.sleep(2)

    def find_play(self):
        return self.find_element(*self.play_video)
    def find_tvtitle(self):
        return self.find_element(*self.tvtitle_video)
    def find_videotitle(self):
        return self.find_element(*self.videotitle_video)
    def find_kvideo(self):
        return self.find_element(*self.kvideo_video)
    def find_cityname(self):
        return self.find_elements(*self.cityname_place)
    def find_titletext(self):
        return self.find_element(*self.titletext_place)
    def find_reflash(self):
        return self.find_element(*self.reflash_place)
    def find_des(self):
        return self.find_element(*self.des_palce)
    def find_dess(self):
        return self.find_elements(*self.des_palce)

    def find_temperaturerange(self):
        return self.find_element(*self.temperature_range_place)

    def find_temperature(self):
        return self.find_element(*self.temperature_place)
    def click_temperature(self):
        self.find_element(*self.temperature_place).click()
        time.sleep(2)

    def find_location(self):
        return self.find_element(*self.location_place)
    def click_location(self):
        self.find_element(*self.location_place).click()
        time.sleep(2)

    def find_webview(self):
        return self.find_element(*self.webview)

    def find_nums(self):
        return self.find_element(*self.nums_picture)

    def click_nums(self):
        self.find_element(*self.nums_picture).click()
        time.sleep(2)

    def find_share(self):
        return self.find_element(*self.share_picture)

    def find_favorite(self):
        return self.find_element(*self.favorite_picture)

    def find_cai(self):
        return self.find_element(*self.cai_picture)

    def click_cai(self):
        self.find_element(*self.cai_picture).click()
        time.sleep(2)

    def find_zan(self):
        return self.find_element(*self.zan_picture)

    def click_zan(self):
        self.find_element(*self.zan_picture).click()
        time.sleep(2)
    def find_kan(self):
        return self.find_element(*self.kan_picture)

    def find_picture(self):
        return self.find_element(*self.beauty_picture)
#点击进入到视频入口

    def click_news_entry(self):
        self.find_element(*self.bottom_news_loc).click()
        time.sleep(3)

#点击视频下方的保存按钮'
    def click_topic (self):
        self.find_element(*self.tv_topic_loc).click()
        time.sleep(2)

    def find_topic (self):
        return self.find_element(*self.tv_topic_loc)


#点击视频下方的分享按钮
    def find_pindaos (self):
        return self.find_elements(*self.textview_loc)


    def find_topics(self):
        return self.find_elements(*self.tv_topic_loc)


    def find_pageviews(self):
        return  self.find_element(*self.pageview_loc)

    def find_source(self):
        return self.find_element(*self.tvsource_loc)

    def click_close(self):
        self.find_element(*self.tvclose_loc).click()
        time.sleep(2)
    def find_comment(self):
        return self.find_element(*self.comment_in)
    def find_hotsin(self):
        return self.find_element(*self.hots_in)

    def find_intitle(self):
        return self.find_element(*self.tvtitle_in)

    def click_inback(self):
        self.find_element(*self.back_in).click()
        time.sleep(3)

    def find_feedback(self):
        return self.find_element(*self.feedback_in)
    def click_feedback(self):
        self.find_element(*self.feedback_in).click()
        time.sleep(2)

    def find_textcontent(self):
        return self.find_elements(*self.textcontent_in)

    def find_seclose(self):
        return self.find_element(*self.seclose_in)

    def find_edit(self):
        return self.find_element(*self.editcontent_in)
    def click_edit(self,words):
        a=self.find_element(*self.editcontent_in)
        a.click()
        a.send_keys(words)
    def find_commit(self):
        return self.find_element(*self.commit_in)
    def click_commit(self):
        self.find_element(*self.commit_in).click()
        time.sleep(2)

    #返回topic的text list
    def topic_list(self):
        add=[]
        for i in range(3):
            e=News(self.driver).find_topics()
            for j in e:
                add.append(j.text)
            Base(self.driver).do_swipe(self.driver,"up")
        return {}.fromkeys(add).keys()

    def click_btncancel(self):
        try:
            self.find_element(*self.iv_close).click()
        #    self.find_element(*self.btn_cancel).click()
        except:
            pass