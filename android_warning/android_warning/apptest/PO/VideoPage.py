#coding:utf-8
from BasePage import Base
import  random
from selenium.webdriver.common.by import  By
import time

class Video(Base):

    #底部的视频按钮

    video_entry_loc = (By.ID,"%s:id/rb_bottom_subscribt"%Base.capabilities['appPackage'])
    save_loc=(By.ID,"%s:id/iv_video_save"%Base.capabilities['appPackage'])
    share_loc=(By.ID,"%s:id/iv_video_share"%Base.capabilities['appPackage'])
    comment_loc=(By.ID,"%s:id/iv_video_comment"%Base.capabilities['appPackage'])
    video_cover_loc=(By.ID,"%s:id/layout_video_cover"%Base.capabilities['appPackage'])
    tv_title_loc=(By.ID,"%s:id/tv_title"%Base.capabilities['appPackage'])
    video_tip=(By.CLASS_NAME,"android.widget.TextView")
    video_title=(By.ID,"%s:id/tv_video_title"%Base.capabilities['appPackage'])
    video_none=(By.ID,"%s:id/layout_info"%Base.capabilities['appPackage'])

    #视频内页：
    tv_command=(By.ID,"%s:id/tv_comment"%Base.capabilities['appPackage'])
    tv_username=(By.ID,"%s:id/tv_username"%Base.capabilities['appPackage'])
    share_pengyouquan=(By.ID,"%s:id/iv_share_weixinpengyou"%Base.capabilities['appPackage'])
    share_weixin=(By.ID,"%s:id/iv_share_weixin"%Base.capabilities['appPackage'])
    share_qq=(By.ID,"%s:id/iv_share_qq"%Base.capabilities['appPackage'])
    share_qzone=(By.ID,"%s:id/iv_share_qzone"%Base.capabilities['appPackage'])
    share_sina=(By.ID,"%s:id/iv_share_sina"%Base.capabilities['appPackage'])
    share_clipboard=(By.ID,"%s:id/iv_share_clipboard"%Base.capabilities['appPackage'])
    fasong=(By.NAME,u"发送")
    fabiao=(By.NAME,u"发表")
    make=(By.NAME,u"创建新聊天")
    name=(By.NAME,"beyond")
    sure=(By.NAME,u"确定(1)")
    share=(By.NAME,u"分享")
    back_df=(By.NAME,u"返回东方头条")
    mine_pc=(By.NAME,u"我的电脑")
    layout_share=(By.ID,"%s:id/layout_share"%Base.capabilities['appPackage'])
    tv_share=(By.ID,"%s:id/tv_share"%Base.capabilities['appPackage'])
    tv_confirm=(By.ID,"%s:id/tv_confirm"%Base.capabilities['appPackage'])
    #-----------------------------------------------------------------
    #信息流内页分享
    def click_tvconfirm(self):
        self.find_element(*self.tv_confirm).click()
        time.sleep(3)

    def click_minepc(self):
        self.find_element(*self.mine_pc).click()
        time.sleep(2)
    def click_fabiao(self):
        self.find_element(*self.fabiao).click()
        time.sleep(3)
    def find_tvshare(self):
        return self.find_element(*self.tv_share)
    def click_tvshare(self):
        self.find_element(*self.tv_share).click()
        time.sleep(2)
    def click_fasong(self):
        self.find_element(*self.fasong).click()
        time.sleep(4)
    def click_name(self):
        self.find_element(*self.name).click()
        time.sleep(1)
    def click_make(self):
        self.find_element(*self.make).click()
        time.sleep(1)
    def click_sure(self):
        self.find_element(*self.sure).click()
        time.sleep(1)
    def click_inshare(self):
        self.find_element(*self.share).click()
        time.sleep(3)
    def click_backdf(self):
        self.find_element(*self.back_df).click()
        time.sleep(2)
    def click_weixin(self):
        self.find_element(*self.share_weixin).click()
        time.sleep(3)
    def click_qq(self):
        self.find_element(*self.share_qq).click()
        time.sleep(3)
    def click_sina(self):
        self.find_element(*self.share_sina).click()
        time.sleep(3)
    def click_clipboard(self):
        self.find_element(*self.share_clipboard).click()
        time.sleep(1)
    def click_qzone(self):
        self.find_element(*self.share_qzone).click()
        time.sleep(3)
    def click_pengyouquan(self):
        self.find_element(*self.share_pengyouquan).click()
        time.sleep(3)

    def click_layoutshare(self):
        self.find_element(*self.layout_share).click()
        time.sleep(2)

    def find_tvcommand(self):
        return self.find_element(*self.tv_command)

    def find_tvusername(self):
        return self.find_element(*self.tv_username)

    def click_videonone(self):
        self.find_element(*self.video_none).click()
        time.sleep(3)

    def find_videotip(self):
        return self.find_elements(*self.video_tip)
#点击进入到视频入口

    def click_video_entry(self):
        self.find_element(*self.video_entry_loc).click()
        time.sleep(3)

#点击视频下方的保存按钮

    def click_save(self):
        self.find_element(*self.save_loc).click()
        time.sleep(2)

#点击视频下方的分享按钮
    def click_share(self):
        self.find_element(*self.share_loc).click()
        time.sleep(2)

#点击视频下方的评论按钮
    def click_comment(self):
        self.find_element(*self.comment_loc).click()
        time.sleep(2)


#点击视频的播放按钮
    def find_video_cover(self):
        return self.find_element(*self.video_cover_loc)



#查找视频列表的标题
    def find_tv_titles(self):
        return self.find_elements(*self.tv_title_loc)

    def find_video_title(self):
        return self.find_element(*self.video_title)