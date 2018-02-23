#coding:utf-8
from BasePage import Base
from Superunit import initunit
import  random

from selenium.webdriver.common.by import  By
import time


class taskcenter(Base):

	tv_sign =(By.ID ,"%s:id/tv_sign"%Base.capabilities['appPackage'])
	tv_todaydate=(By.ID,"%s:id/tv_today_date"%Base.capabilities['appPackage'])
	tv_has_signed= (By.ID ,"%s:id/tv_has_signed_days"%Base.capabilities['appPackage'])
	sign_back = (By.ID ,"%s:id/ll_widgetTitleBar_left"%Base.capabilities['appPackage'])
	sign_rule = (By.ID ,"%s:id/tv_sign_rule"%Base.capabilities['appPackage'])

	sign_date = (By.ID ,"%s:id/tv_date"%Base.capabilities['appPackage'])
	sign_today  = (By.ID ,"%s:id/tv_sign_today"%Base.capabilities['appPackage'])
	iv_close=(By.ID,"%s:id/iv_close"%Base.capabilities['appPackage'])
	luckybag=(By.ID,"%s:id/rl_lucklycontent"%Base.capabilities['appPackage'])
	tasktext=(By.ID,"%s:id/tv_titleBarWidget_titelText"%Base.capabilities['appPackage'])
	invite_fs=(By.NAME,u"邀请好友")
	invite_num=(By.ID,"%s:id/tv_invite_number"%Base.capabilities['appPackage'])
	invite_share=(By.ID,"%s:id/tv_share"%Base.capabilities['appPackage'])
	daily_task_state=(By.NAME,u"未完成")
	tv_detail=(By.ID,"%s:id/tv_detail"%Base.capabilities['appPackage'])
	read_title=(By.NAME,u"阅读文章")
	read_news=(By.NAME,u"阅读新闻")
	share_title=(By.NAME,u"分享新闻")
	show_news=(By.NAME,u"发表评论")
	show_title=(By.NAME,u"评论文章")

	fashion_shareread=(By.NAME,u"分享被阅读")
	copy_invitenum=(By.ID,"%s:id/tv_copy"%Base.capabilities['appPackage'])
	fasong=(By.NAME,u"发表")
	invite_rule=(By.NAME,u"邀请规则")
	qq_spaceshare=(By.ID,"%s:id/iv_share_qzone"%Base.capabilities['appPackage'])

	new_person=(By.NAME,u"新人专享")
	new_ownchannel=(By.NAME,u"订阅专属频道")
	new_bangding=(By.NAME,u"绑定账号")
	new_regist=(By.NAME,u"注册有礼")
	new_firstshare=(By.NAME,u"首次分享")
	new_rewardback=(By.NAME,u"有奖反馈")
	new_subchannel=(By.ID,"%s:id/btn_toSubscribt"%Base.capabilities['appPackage'])

	def find_tvtodaydate(self):
		return self.find_element(*self.tv_todaydate)

	#--------------------------------------------------------------
	#新人专享模块
	def find_newperson(self):
		return self.find_element(*self.new_person)
	def find_newownchannel(self):
		return self.find_element(*self.new_ownchannel)
	def click_newownchannel(self):
		self.find_element(*self.new_ownchannel).click()
		time.sleep(1)
	def find_newbangding(self):
		return self.find_element(*self.new_bangding)
	def click_newbangding(self):
		self.find_element(*self.new_bangding).click()
		time.sleep(1)
	def find_newregist(self):
		return self.find_element(*self.new_regist)
	def click_newregist(self):
		self.find_element(*self.new_regist).click()
		time.sleep(1)
	def find_newfirstshare(self):
		return self.find_element(*self.new_firstshare)
	def click_newfirstshare(self):
		self.find_element(*self.new_firstshare).click()
		time.sleep(1)
	def find_newrewardback(self):
		return self.find_element(*self.new_rewardback)
	def click_newrewardback(self):
		self.find_element(*self.new_rewardback).click()
		time.sleep(1)
	def click_newsubchannel(self):
		self.find_element(*self.new_subchannel).click()
		time.sleep(2)
	#-----------------------------------------------------------------
	#每日任务
	def find_readtitle(self):
		return self.find_element(*self.read_title)
	def find_sharetitle(self):
		return self.find_element(*self.share_title)
	def find_showtitle(self):
		return self.find_element(*self.show_title)

	def click_sharenews(self):
		self.find_element(*self.share_title).click()
		time.sleep(1)
	def click_shownews(self):
		self.find_element(*self.show_news).click()
		time.sleep(1)
	def click_readnews(self):
		self.find_element(*self.read_news).click()
		time.sleep(1)
	#---------------------------------------------------------
	#达人奖励
	def click_fashion_shareread(self):
		self.find_element(*self.fashion_shareread).click()
		time.sleep(1)
	def find_fashion_shareread(self):
		return self.find_element(*self.fashion_shareread)

	def click_copynum(self):
		self.find_element(*self.copy_invitenum).click()

	def click_inviterule(self):
		self.find_element(*self.invite_rule).click()
		time.sleep(1)
	def click_qqspaceshare(self):
		self.find_element(*self.qq_spaceshare).click()
		time.sleep(5)
	def click_fasong(self):
		self.find_element(*self.fasong).click()
		time.sleep(2)
	#------------------------------------------------------------
	def find_dailystate(self):
		return self.find_element(*self.daily_task_state)
	def find_tvdetails(self):
		return self.find_elements(*self.tv_detail)
	def find_inviteshares(self):
		return self.find_elements(*self.invite_share)
	def find_invitenum(self):
		return self.find_element(*self.invite_num)
	def click_invitefs(self):
		self.find_element(*self.invite_fs).click()
		time.sleep(1)
	def find_invitefs(self):
		return self.find_element(*self.invite_fs)

	def find_tasktext(self):
		return self.find_element(*self.tasktext)
	def click_iv_close(self):
		self.find_element(*self.iv_close).click()
		time.sleep(1)

	def find_sign_ele(self):
		return  self.find_element(*self.tv_has_signed).get_attribute('name')


	def click_back(self):
		self.find_element(*self.sign_back).click()


	def find_login_el(self):
		return self.find_element(*self.tv_sign)

	def click_login_el(self):
		self.find_element(*self.tv_sign).click()
		time.sleep(3)

	def find_signtoday_el(self):
		return  self.find_element(*self.sign_today).get_attribute('name')

	def find_luckybag(self):
		return self.find_element(*self.luckybag)