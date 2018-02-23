#coding:utf-8
from BasePage import Base
from selenium.webdriver.common.by import  By
import time

class Discovery(Base):


    lucky_str1=u"幸运夺宝天天有惊喜幸运夺宝 Link"
    lucky_str2=u"幸运夺宝-界面异常"
    lucky_str3=[u"幸运夺宝",u"我的夺宝 Link",u"夺宝 Link",u"晒单 Link",u"热门商品 Heading"]


    shop_str1=u"积分商城热销商品积分商城 Link"
    shop_str2=u"积分商城-界面异常"
    shop_str3=[u"积分商城",u"小积分大价值",u"直充类 Link",u"兑换记录 Link"]



    spike_str1=u"秒杀10元话费秒杀 Link"
    spike_str2=u"限时秒杀-界面异常"
    spike_str3=[u"秒杀专区"]

    content_view="WEBVIEW_com.songheng.eastnews"

    xpath_list=["//*[@id='contentBcnt']/div[1]/div/div[1]","//*[@id='contentBcnt']/div[1]/div/div[2]","//*[@id='contentBcnt']/div[1]/div/div[3]"]


    found_entry_loc= (By.ID ,"%s:id/tv_found"%Base.capabilities['appPackage'])

    activity_loc = (By.ID ,"%s:id/rb_activity"%Base.capabilities['appPackage'])

    back_loc =(By.ID,"%s:id/imgbtn_titlebar_left"%Base.capabilities['appPackage'])
    webview_xpath_loc= (By.XPATH,"//*[@id='fixedabtn']")
    webview_byid_loc =(By.TAG_NAME,"li")
    view_page=(By.ID,"%s:id/viewpager"%Base.capabilities['appPackage'])

    def find_viewpage(self):
        return self.find_element(*self.view_page)

    def click_foundentry(self):
        self.find_element(*self.found_entry_loc).click()
        time.sleep(10)

    def click_activity(self):
        self.find_element(*self.activity_loc).click()
        time.sleep(5)


    def click_back(self):
        self.find_element(*self.back_loc).click()


    def find_webviewxpath_el(self):
        return self.find_element(*self.webview_xpath_loc)

    def find_webviewid_el(self):
        return self.find_element(*self.webview_byid_loc)