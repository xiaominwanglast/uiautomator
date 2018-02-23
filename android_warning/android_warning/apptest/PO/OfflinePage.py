#coding:utf-8
from BasePage import Base

import  random

from selenium.webdriver.common.by import  By
import time

class page(Base):

	download_id_loc =(By.ID ,"%s:id/layout_download"%Base.capabilities['appPackage'])
	back_id_loc = (By.ID ,"%s:id/iv_back"%Base.capabilities['appPackage'])

	iv_switch_loc =(By.ID ,"%s:id/iv_switch"%Base.capabilities['appPackage'])
	tv_title_loc= (By.ID ,"%s:id/tv_title"%Base.capabilities['appPackage'])

	dl_click_loc =(By.ID ,"%s:id/layout_download"%Base.capabilities['appPackage'])
	tv_topic_loc = (By.ID ,"%s:id/tv_topic"%Base.capabilities['appPackage'])
	tv_more_loc = (By.ID ,"%s:id/tv_more"%Base.capabilities['appPackage'])
	tv_state_loc = (By.ID ,"%s:id/tv_state"%Base.capabilities['appPackage'])

	layout_bg_loc = (By.ID ,"%s:id/layout_bg"%Base.capabilities['appPackage'])
	ll_item_loc = (By.ID ,"%s:id/ll_item"%Base.capabilities['appPackage'])
	ll_item1_loc = (By.ID ,"%s:id/ll_item1"%Base.capabilities['appPackage'])
	tv_share = (By.ID ,"%s:id/tv_shareTitle"%Base.capabilities['appPackage'])

	dl_back_loc = (By.ID ,"%s:id/ll_back"%Base.capabilities['appPackage'])

	def click_downloadid(self):
		self.find_element(*self.download_id_loc).click()
		time.sleep(2)

	def find_dlclickloc(self):
		return self.find_element(*self.dl_click_loc)

	def click_back(self):
		self.find_element(*self.back_id_loc).click()
		time.sleep(2)


	def click_iv_switch(self):
		self.find_element(*self.iv_switch_loc).click()
		time.sleep(2)

	def  find_switch_buttons(self):
		return  self.find_elements(*self.iv_switch_loc)

	def find_tv_el(self):
		return  self.find_elements(*self.tv_title_loc)


	def click_dlbutton(self):
		self.find_element(*self.tv_state_loc).click()


	def find_dlpage_els(self):
		return  self.find_elements(*self.tv_topic_loc)


	def find_nums(self):
		return  self.find_element(*self.tv_more_loc).get_attribute('name')[7:9]

	def find_els_more(self):
		return self.find_element(*self.tv_more_loc)

	def click_more(self):
		self.find_element(*self.tv_more_loc).click()
		time.sleep(2)

	def find_pinluns_el(self):
		return  self.find_elements(*self.layout_bg_loc)

	def find_tvshare(self):
		return self.find_elements(*self.tv_share)


	def find_state_el(self):
		return  self.find_element(*self.tv_state_loc).get_attribute('name')

	def click_dl_back(self):
		self.find_element(*self.dl_back_loc).click()
		time.sleep(2)
