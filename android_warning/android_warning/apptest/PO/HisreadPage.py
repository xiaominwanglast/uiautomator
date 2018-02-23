#coding:utf-8
from BasePage import Base



from selenium.webdriver.common.by import  By
import time
import random

class Hisread(Base):
	clear_loc =(By.ID ,"%s:id/tv_titleBarWidget_rightBtn"%Base.capabilities['appPackage'])
	back_loc = (By.ID ,"%s:id/imgbtn_titlebar_left"%Base.capabilities['appPackage'])
	title_loc = (By.ID ,"%s:id/text_titlebar_title"%Base.capabilities['appPackage'])

	news_title_loc = (By.ID ,"%s:id/tv_topic"%Base.capabilities['appPackage'])

	tv_confirm_loc = (By.ID ,"%s:id/tv_confirm"%Base.capabilities['appPackage'])

	tv_cancel_loc = (By.ID ,"%s:id/tv_cancel"%Base.capabilities['appPackage'])

	tv_readnews_loc = (By.ID ,"%s:id/tv_read_news"%Base.capabilities['appPackage'])

	def  click_clear(self):
		self.find_element(*self.clear_loc).click()
		time.sleep(2)
	def find_clear(self):
		return self.find_element(*self.clear_loc)

	def click_back(self):
		self.find_element(*self.back_loc).click()
		time.sleep(2)


	def find_news_msg(self):
		return  self.find_element(*self.news_title_loc)


	def click_cofirm(self):
		self.find_element(*self.tv_confirm_loc).click()
		time.sleep(2)


	def click_cancel(self):
		self.find_element(*self.tv_cancel_loc).click()
		time.sleep(2)

	def click_tvreadnews(self):
		self.find_element(*self.tv_readnews_loc).click()
		time.sleep(2)
	def find_tvreadnews(self):
		return self.find_element(*self.tv_readnews_loc)