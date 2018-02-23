#coding:utf-8
from BasePage import Base



from selenium.webdriver.common.by import  By
import time
import random

class Mine(Base):

    mine_loc =(By.ID ,"%s:id/rb_bottom_mine"%Base.capabilities['appPackage'])
    purse_loc =(By.ID ,"%s:id/rl_integral"%Base.capabilities['appPackage'])
    loginbutton_loc = (By.ID,"%s:id/tv_login"%Base.capabilities['appPackage'])
    back_loc = (By.ID,'%s:id/imgbtn_titlebar_left'%Base.capabilities['appPackage'])
    text_title_loc = (By.ID,'%s:id/text_titlebar_title'%Base.capabilities['appPackage'])
    mall_loc =(By.ID,'%s:id/rl_mall'%Base.capabilities['appPackage'])
    new_login=(By.ID,'%s:id/tv_login_hint'%Base.capabilities['appPackage'])

    mall_list=[u"直充类 Link",u"实物类 Link",u"优惠券 Link",u"兑换记录 Link"]
    mine_nologin_list=[u"未登录",u"收藏",u"钱包",u"商城",u"消息",u"邀请码",u"历史阅读",u"任务中心"]
    mine_login_list=[u"收藏",u"钱包",u"商城",u"消息",u"邀请码",u"历史阅读",u"任务中心"]
    class_view_loc="android.view.View"


    #列出消息，邀请码，历史阅读，任务中心等按钮
    tv_notify_loc = (By.ID,'%s:id/tv_notify'%Base.capabilities['appPackage'])
    tv_invite_friends = (By.ID,'%s:id/tv_invite_friends'%Base.capabilities['appPackage'])
    tv_give_integral = (By.ID,'%s:id/tv_give_integral'%Base.capabilities['appPackage'])
    tv_history_read = (By.ID,'%s:id/tv_history_read'%Base.capabilities['appPackage'])
    tv_task_center = (By.ID,'%s:id/tv_task_center'%Base.capabilities['appPackage'])
    tv_sign_earn_integral = (By.ID,'%s:id/tv_sign_earn_integral'%Base.capabilities['appPackage'])
    tv_download_toggle =  (By.NAME,u'离线阅读')
    tv_night_toggle = (By.ID,'%s:id/tv_night_toggle'%Base.capabilities['appPackage'])
    iv_night_toggle=(By.ID,'%s:id/iv_night_toggle'%Base.capabilities['appPackage'])
    tv_setting = (By.ID,'%s:id/iv_setting'%Base.capabilities['appPackage'])
    tv_feedback = (By.ID,'%s:id/tv_feedback'%Base.capabilities['appPackage'])
    tasknotify=(By.NAME,u"3个任务未完成")
    img_newmsg = (By.ID,'%s:id/img_newmsg'%Base.capabilities['appPackage'])
    login_tip=(By.ID,"%s:id/tv_login_tip"%Base.capabilities['appPackage'])
    ivuser_image=(By.ID,"%s:id/iv_usr_image"%Base.capabilities['appPackage'])
    despoil=(By.ID,"%s:id/ll_despoil_treasure"%Base.capabilities['appPackage'])
    no_image=(By.ID,"%s:id/forward_no_image"%Base.capabilities['appPackage'])
    image_back=(By.NAME,u"返回")
    #积分商城
    mall_title=(By.NAME,u"积分商城")
    despoil_title=(By.NAME,u"幸运夺宝")
    #推送
    news_push=(By.ID,'%s:id/tv_push_news'%Base.capabilities['appPackage'])
    def click_tuisongnews(self):
        self.find_element(*self.news_push).click()
        time.sleep(8)

    def click_newlogin(self):
        self.find_element(*self.new_login).click()
        time.sleep(1)

    def find_imageback(self):
        return self.find_element(*self.image_back)

    def find_malltitle(self):
        return self.find_element(*self.mall_title)
    def find_despoiltitle(self):
        return self.find_element(*self.despoil_title)

    def click_noimage(self):
        self.find_element(*self.no_image).click()
        time.sleep(1)
    def find_despoil(self):
        return self.find_element(*self.despoil)
    def click_despoil(self):
        self.find_element(*self.despoil).click()
        time.sleep(10)

    def find_tasknotify(self):
        return self.find_element(*self.tasknotify)
    def find_tasknotifyID(self):
        return self.find_element(*self.tv_sign_earn_integral)

    def find_logintip(self):
        return self.find_element(*self.login_tip)

    def click_userimage(self):
        self.find_element(*self.ivuser_image).click()
        time.sleep(2)
#进入到我的界面
    def click_mine_entry(self):
        self.find_element(*self.mine_loc).click()
        time.sleep(2)

    #点击钱包按钮
    def click_purse(self):
        self.find_element(*self.purse_loc).click()
        time.sleep(10)
    def find_purse(self):
        return self.find_element(*self.purse_loc)

    def find_title(self):
        return  self.find_element(*self.text_title_loc)

#返回登录按钮元素
    def find_loginbutton(self):
        return  self.find_element(*self.loginbutton_loc)

#点击返回按钮
    def click_back(self):
        self.find_element(*self.back_loc).click()
        time.sleep(2)

#点击商城按钮
    def click_mall(self):
        self.find_element(*self.mall_loc).click()
        time.sleep(10)

    def find_mall(self):
        return self.find_element(*self.mall_loc)

    def click_msg(self):
        self.find_element(*self.tv_notify_loc).click()
        time.sleep(2)
    def find_msg(self):
        return self.find_element(*self.tv_notify_loc)

    def click_invite(self):
        self.find_element(*self.tv_invite_friends).click()
        time.sleep(4)
    def find_invite(self):
        return self.find_element(*self.tv_invite_friends)

    def click_hisred(self):
        self.find_element(*self.tv_history_read).click()
        time.sleep(2)
    def find_hisred(self):
        return self.find_element(*self.tv_history_read)

    def click_task(self):
        self.find_element(*self.tv_task_center).click()
        time.sleep(5)
    def find_task(self):
        return self.find_element(*self.tv_task_center)

    def click_offline(self):
        print self.find_element(*self.tv_download_toggle)
        self.find_element(*self.tv_download_toggle).click()

        time.sleep(2)
    def find_offline(self):
        return self.find_element(*self.tv_download_toggle)

    def click_night(self):
        self.find_element(*self.iv_night_toggle).click()
        time.sleep(3)
    def find_night(self):
        return self.find_element(*self.tv_night_toggle)

    def click_set(self):
        self.find_element(*self.tv_setting).click()
        time.sleep(2)
    def find_set(self):
        return self.find_element(*self.tv_setting)

    def click_feedback(self):
        self.find_element(*self.tv_feedback).click()
        time.sleep(6)
    def find_feedback(self):
        return self.find_element(*self.tv_feedback)

    def find_newmsg_els(self):
        return self.find_elements(*self.img_newmsg)
