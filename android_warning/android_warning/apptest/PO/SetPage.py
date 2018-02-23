#coding:utf-8
from BasePage import Base
from random import randint

from selenium.webdriver.common.by import By
import time

class Set(Base):
	tv_clear_loc=(By.ID,"%s:id/tv_clear_buffer"%Base.capabilities['appPackage'])
	tv_size_loc = (By.ID,"%s:id/tv_size"%Base.capabilities['appPackage'])
	clear_ok_loc =(By.ID,"%s:id/download_clear_ok"%Base.capabilities['appPackage'])
	body_size=(By.ID,"%s:id/tv_font_size"%Base.capabilities['appPackage'])
	clear_cancle_loc =(By.ID,"%s:id/download_clear_cancel"%Base.capabilities['appPackage'])
	back_loc = (By.ID,"%s:id/ll_widgetTitleBar_left"%Base.capabilities['appPackage'])
	iv_notify=(By.ID,"%s:id/iv_notify_toggle"%Base.capabilities['appPackage'])
	tv_version=(By.ID,"%s:id/tv_about_version"%Base.capabilities['appPackage'])
	tv_account=(By.ID,"%s:id/tv_bound_account"%Base.capabilities['appPackage'])

	#账户设置
	head_img=(By.ID,"%s:id/img_head"%Base.capabilities['appPackage'])
	edit_name=(By.ID,"%s:id/edit_nickname"%Base.capabilities['appPackage'])
	edit_boy=(By.ID,"%s:id/radio_boy"%Base.capabilities['appPackage'])
	edit_girl=(By.ID,"%s:id/radio_girl"%Base.capabilities['appPackage'])
	edit_secret=(By.ID,"%s:id/radio_secret"%Base.capabilities['appPackage'])
	name=(By.NAME,u"昵称")
	sex=(By.NAME,u"性别")
	account=(By.NAME,u"绑定社交账号")
	jiebang=(By.NAME,u"解绑")
	bangding=(By.NAME,u"点击绑定")
	tip=(By.NAME,u"解绑该账号积分将被清零，确认解绑?")
	tv_phone=(By.ID,"%s:id/tv_phone"%Base.capabilities['appPackage'])
	rl_QQ=(By.ID,"%s:id/rl_qq"%Base.capabilities['appPackage'])
	btn_submit=(By.ID,"%s:id/btn_submit"%Base.capabilities['appPackage'])
	right_change=(By.NAME,u"切换帐号")
	tv_login=(By.ID,"%s:id/tv_login"%Base.capabilities['appPackage'])
	tv_cancel=(By.ID,"%s:id/tv_cancel"%Base.capabilities['appPackage'])
	def click_tvcancel(self):
		self.find_element(*self.tv_cancel).click()
		time.sleep(1)
	def find_tip(self):
		return self.find_element(*self.tip)
	def click_tvlogin(self):
		self.find_element(*self.tv_login).click()
		time.sleep(3)
	def find_jiebang(self):
		return self.find_element(*self.jiebang)

	def find_bangding(self):
		return self.find_elements(*self.bangding)

	def click_jiebang(self):
		self.find_element(*self.jiebang).click()
		time.sleep(5)
	def click_right(self):
		self.find_element(*self.right_change).click()
		time.sleep(2)
	def input_editname(self,keywords):
		self.find_element(*self.edit_name).send_keys(keywords)
		time.sleep(2)
	def click_boy(self):
		self.find_element(*self.edit_boy).click()
		time.sleep(1)
	def click_girl(self):
		self.find_element(*self.edit_girl).click()
		time.sleep(1)
	def click_secret(self):
		self.find_element(*self.edit_secret).click()
		time.sleep(1)
	def click_btn(self):
		self.find_element(*self.btn_submit).click()
		time.sleep(3)
	def find_rlQQ(self):
		return self.find_element(*self.rl_QQ)
	def click_rlQQ(self):
		self.find_element(*self.rl_QQ).click()
		time.sleep(6)
	def find_phone(self):
		return self.find_element(*self.tv_phone)
	def find_name(self):
		return self.find_element(*self.name)
	def find_sex(self):
		return self.find_element(*self.sex)
	def find_account(self):
		return self.find_element(*self.account)
	def find_headimg(self):
		return self.find_element(*self.head_img)

	def click_tvaccount(self):
		self.find_element(*self.tv_account).click()
		time.sleep(2)
	def find_tv_version(self):
		return self.find_element(*self.tv_version)
	def click_iv_notify(self):
		self.find_element(*self.iv_notify).click()
		time.sleep(2)

	def click_clear(self):
		self.find_element(*self.tv_clear_loc).click()



	def get_el_size(self):
		return  self.find_element(*self.tv_size_loc).get_attribute('name')


	def click_clear_ok(self):

		self.find_element(*self.clear_ok_loc).click()

	def click_back(self):
		self.find_element(*self.back_loc).click()

	def click_bodysize(self):
		self.find_element(*self.body_size).click()
		time.sleep(1)
	def find_bodysize(self):
		return self.find_element(*self.body_size)

	def click_clear_cancle(self):
		self.find_element(*self.clear_cancle_loc).click()

#		self.find_element(*self.clear_cancle_loc).click()




