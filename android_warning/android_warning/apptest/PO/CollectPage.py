#coding:utf-8
import time
from BasePage import Base
from selenium.webdriver.common.by import By

class Collect(Base):
    #收藏界面元素
    mine=(By.ID,"%s:id/rb_bottom_mine"%Base.capabilities['appPackage'])
    mine_collect=(By.ID,"%s:id/rl_favorite"%Base.capabilities['appPackage'])

    tv_text=(By.NAME,u"资讯")
    tv_image=(By.NAME,u"图片")
    tv_video=(By.NAME,u"视频")

    tv_topic=(By.ID,"%s:id/tv_topic"%Base.capabilities['appPackage'])
    tv_videotitle=(By.ID,"%s:id/tv_video_title"%Base.capabilities['appPackage'])
    #返回
    back_loc=(By.ID,"%s:id/ll_widgetTitleBar_left"%Base.capabilities['appPackage'])
    #收藏
#    collect=(By.ID,"%s:id/text_titlebar_title"%Base.capabilities['appPackage'])
    #编辑
    edit_loc=(By.ID,"%s:id/tv_titleBarWidget_rightBtn"%Base.capabilities['appPackage'])

    #新闻页
    save_page=(By.ID,"%s:id/layout_save"%Base.capabilities['appPackage'])

    #新闻页返回
    page_back=(By.ID,"%s:id/back"%Base.capabilities['appPackage'])

    #新闻界面添加频道
    add_newchannel=(By.ID,"%s:id/iv_news_arrow"%Base.capabilities['appPackage'])

    #频道界面添加
    channel_add=(By.ID,"%s:id/iv_add_subscribe"%Base.capabilities['appPackage'])

    #频道搜索
    channel_search=(By.ID,"%s:id/tv_search"%Base.capabilities['appPackage'])

    #编辑搜索
    search_edit=(By.ID,"%s:id/edit_search"%Base.capabilities['appPackage'])

    #点击搜索按钮
    btn_search=(By.ID,"%s:id/btn_search"%Base.capabilities['appPackage'])

    #点击订阅
    btn_subscribe=(By.ID,"%s:id/btn_subscribe"%Base.capabilities['appPackage'])

    #收藏图片
    favorite_image=(By.ID,"%s:id/iv_favorite"%Base.capabilities['appPackage'])

    #视频分享
    video_share=(By.ID,"%s:id/iv_video_share"%Base.capabilities['appPackage'])

    #视频收藏
    video_save=(By.ID,"%s:id/iv_video_save"%Base.capabilities['appPackage'])

    #视屏入口
    video_enter=(By.ID,"%s:id/rb_bottom_subscribt"%Base.capabilities['appPackage'])

    video_comment_loc = (By.ID,"%s:id/iv_video_comment"%Base.capabilities['appPackage'])

    video_title_loc = (By.ID,"%s:id/tv_video_title"%Base.capabilities['appPackage'])


    cb_del_loc = (By.ID,"%s:id/cb_delete"%Base.capabilities['appPackage'])

    btn_del_loc = (By.ID,"%s:id/btn_del"%Base.capabilities['appPackage'])

    btn_selectall_loc = (By.ID,"%s:id/btn_selectall"%Base.capabilities['appPackage'])

    def click_video_enter(self):
        self.find_element(*self.video_enter).click()
        time.sleep(3)


    def find_els_videossave(self):
        return  self.find_elements(*self.video_save)

    def click_video_save(self):
        self.find_element(*self.video_save).click()
        time.sleep(2)

    def find_video_share(self):
        return self.find_element(*self.video_share)

    def click_favorite_image(self):
        self.find_element(*self.favorite_image).click()
        time.sleep(2)

    def find_favorite_image(self):
        return self.find_element(*self.favorite_image)

    def click_btn_subscribe(self):
        self.find_element(*self.btn_subscribe).click()
        time.sleep(2)

    def click_btn_search(self):
        self.find_element(*self.btn_search).click()
        time.sleep(2)

    def click_search_edit(self):
        return self.find_element(*self.search_edit)

    def click_channel_search(self):
        self.find_element(*self.channel_search).click()
        time.sleep(4)

    def click_channel_add(self):
        self.find_element(*self.channel_add).click()
        time.sleep(2)

    def click_add_channel(self):
        self.find_element(*self.add_newchannel).click()
        time.sleep(2)

    def click_page_back(self):
        self.find_element(*self.page_back).click()
        time.sleep(2)

    def click_save_page(self):
        self.find_element(*self.save_page).click()
        time.sleep(2)

    def click_mine(self):
        self.find_element(*self.mine).click()
        time.sleep(2)
    def find_mine_collect(self):
        return self.find_element(*self.mine_collect)

    def click_mine_collect(self):
        self.find_element(*self.mine_collect).click()
        time.sleep(2)

    def click_tv_text(self):
        self.find_element(*self.tv_text).click()
        time.sleep(2)
    def find_tv_text(self):
        return self.find_element(*self.tv_text)

    def click_tv_image(self):
        self.find_element(*self.tv_image).click()
        time.sleep(2)
    def find_tv_image(self):
        return self.find_element(*self.tv_image)

    def click_tv_video(self):
        self.find_element(*self.tv_video).click()
        time.sleep(2)
    def find_tv_video(self):
        return self.find_element(*self.tv_video)

    def find_topic(self):
        return self.find_element(*self.tv_topic)

    def find_topics(self):
        return self.find_elements(*self.tv_topic)

    def click_one_Topic(self):
        self.find_element(*self.tv_topic).click()

        time.sleep(2)

    def click_back(self):
        self.find_element(*self.back_loc).click()
        time.sleep(2)

    def click_edit(self):
        self.find_element(*self.edit_loc).click()
        time.sleep(2)

    def find_videotitles(self):
        return self.find_elements(*self.tv_videotitle)


    def find_els_comment(self):
        return  self.find_elements(*self.video_comment_loc)
    def click_els_comment(self):
        self.find_element(*self.video_comment_loc).click()
        time.sleep(2)

    def find_titles_video(self):
        return  self.find_elements(*self.video_title_loc)



    def find_els_cbdel(self):
        return  self.find_elements(*self.cb_del_loc)


    def click_btn_del(self):
        self.find_element(*self.btn_del_loc).click()
        time.sleep(1)


    def click_select_all(self):
        self.find_element(*self.btn_selectall_loc).click()
        time.sleep(1)


