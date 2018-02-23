#coding:utf-8
from BasePage import Base



from selenium.webdriver.common.by import  By
import time
import random

class purse(Base):
	purse_tv_current_loc= (By.ID,'%s:id/tv_current'%Base.capabilities['appPackage'])
	purse_total_bonus_loc = (By.ID,'%s:id/total_bonus'%Base.capabilities['appPackage'])
	purse_yesterday_bonus_loc = (By.ID,'%s:id/yesterday_bonus'%Base.capabilities['appPackage'])
	purse_historybonus=(By.ID,"%s:id/tv_history_bonus"%Base.capabilities['appPackage'])
	purse_back_loc = (By.ID,'%s:id/ll_widgetTitleBar_left'%Base.capabilities['appPackage'])
	drawmoney=(By.NAME,u"提现")
	zhifubao_text=(By.NAME,u"积分夺宝充值")
	purse_money=(By.NAME,u"可提现金额（元）")
	purse_historyget=(By.NAME,u"历史收入")
	purse_incomerule=(By.NAME,u"积分规则")
	purse_incomedetails=(By.NAME,u"收支明细")

	purse_invite=(By.ID,"%s:id/tv_friends_rewards"%Base.capabilities['appPackage'])
	tv_bouns=(By.ID,"%s:id/tv_bonus"%Base.capabilities['appPackage'])
	tv_item=(By.ID,"%s:id/tv_item_name"%Base.capabilities['appPackage'])
	close=(By.ID,"%s:id/tv_titleBarWidget_leftSecondBtn"%Base.capabilities['appPackage'])
	#邀请奖励界面
	tv_number=(By.ID,"%s:id/tv_total_number"%Base.capabilities['appPackage'])
	divide_reward=(By.ID,"%s:id/radio_divide_reward"%Base.capabilities['appPackage'])
	giftbag=(By.ID,"%s:id/radio_giftbag"%Base.capabilities['appPackage'])
	reward_rule=(By.ID,"%s:id/tv_rewards_rule"%Base.capabilities['appPackage'])
	divide_reward_rule=(By.ID,"%s:id/tv_divide_rewards_rule"%Base.capabilities['appPackage'])

	def find_purse_historybonus(self):
		return self.find_element(*self.purse_historybonus).get_attribute('name')

	def click_dividerewardrule(self):
		self.find_element(*self.divide_reward_rule).click()
		time.sleep(2)
	def find_tvnumber(self):
		return self.find_element(*self.tv_number)
	def find_dividereward(self):
		return self.find_element(*self.divide_reward)
	def find_giftbag(self):
		return self.find_element(*self.giftbag)
	def click_giftbag(self):
		self.find_element(*self.giftbag).click()
		time.sleep(1)
	def find_rewardrule(self):
		return self.find_element(*self.reward_rule)
	def find_close(self):
		return self.find_element(*self.close)
	def find_tvitem(self):
		return self.find_elements(*self.tv_item)
	def find_tvbouns(self):
		return self.find_elements(*self.tv_bouns)
	def find_incomerule(self):
		return self.find_element(*self.purse_incomerule)
	def click_incomerule(self):
		self.find_element(*self.purse_incomerule).click()
		time.sleep(3)

	def find_incomedetail(self):
		return self.find_element(*self.purse_incomedetails)
	def find_invite(self):
		return self.find_element(*self.purse_invite)
	def click_invite(self):
		self.find_element(*self.purse_invite).click()
		time.sleep(3)

	def find_pursehistoryget(self):
		return self.find_element(*self.purse_historyget)
	def find_pursemoney(self):
		return self.find_element(*self.purse_money)
	def click_drawmoney(self):
		self.find_element(*self.drawmoney).click()
		time.sleep(6)
	def find_zhifubaotext(self):
		return self.find_element(*self.zhifubao_text)

	def find_login_tv_current(self):
		return  self.find_element(*self.purse_tv_current_loc)


	def find_login_total_bonus(self):
		return  self.find_element(*self.purse_total_bonus_loc).get_attribute('name')


	def find_login_yesterday_bonus(self):
		return  self.find_element(*self.purse_yesterday_bonus_loc).get_attribute('name')
	def find_yesterday_bonus(self):
		return  self.find_element(*self.purse_yesterday_bonus_loc)

	def click_back(self):
		self.find_element(*self.purse_back_loc).click()

