#coding:utf-8
from BasePage import Base
import random

from selenium.webdriver.common.by import By
import time

class Inside(Base):
	back_loc=(By.ID,"%s:id/back"%Base.capabilities['appPackage'])
	config_loc =(By.ID,"%s:id/iv_titlebar_config"%Base.capabilities['appPackage'])
	save_loc = (By.ID,"%s:id/layout_save"%Base.capabilities['appPackage'])
	share_loc = (By.ID,"%s:id/layout_share"%Base.capabilities['appPackage'])

	config_loc_other=(By.ID,"%s:id/iv_font_setting"%Base.capabilities['appPackage'])


	def click_back(self):
		self.find_element(*self.back_loc).click()
		time.sleep(2)

	def find_configloc(self):
		return self.find_elements(*self.config_loc)
	def find_configloc_other(self):
		return self.find_elements(*self.config_loc_other)