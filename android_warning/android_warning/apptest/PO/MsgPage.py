#coding:utf-8
from BasePage import Base



from selenium.webdriver.common.by import  By
import time
import random

class Msg(Base):

	msg_edit_loc =(By.ID ,"%s:id/tv_titleBarWidget_rightBtn"%Base.capabilities['appPackage'])
	#消息标题，内容，时间
	msg_title_loc =(By.ID ,"%s:id/txt_title"%Base.capabilities['appPackage'])
	msg_summary_loc = (By.ID ,"%s:id/txt_summary"%Base.capabilities['appPackage'])
	msg_data_loc = (By.ID ,"%s:id/txt_date"%Base.capabilities['appPackage'])

	msg_selectall_loc = (By.ID ,"%s:id/tv_select_all"%Base.capabilities['appPackage'])
	msg_del_loc = (By.ID ,"%s:id/tv_delete"%Base.capabilities['appPackage'])
	msg_el_del_loc = (By.ID ,"%s:id/cb_delete"%Base.capabilities['appPackage'])
	tv_content=(By.ID,"%s:id/tv_content"%Base.capabilities['appPackage'])
	inmsg_title=(By.ID,"%s:id/tv_titleBarWidget_titelText"%Base.capabilities['appPackage'])
	#评论界面
	commant_title=(By.NAME,u"评论")
	zan_title=(By.NAME,u"赞")
	comment_img=(By.ID,"%s:id/iv_avatar"%Base.capabilities['appPackage'])
	comment_text=(By.ID,"%s:id/tv_comment"%Base.capabilities['appPackage'])
	comment_reply=(By.ID,"%s:id/tv_comment_reply"%Base.capabilities['appPackage'])
	comment_newstitle=(By.ID,"%s:id/tv_news_title"%Base.capabilities['appPackage'])
	#赞界面
	zan_nickname=(By.ID,"%s:id/tv_nickname"%Base.capabilities['appPackage'])
	tv_title=(By.ID,"%s:id/tv_title"%Base.capabilities['appPackage'])

	def find_tvtitles(self):
		return self.find_elements(*self.tv_title)
	def find_zannames(self):
		return self.find_elements(*self.zan_nickname)
	def find_comment_newstitle(self):
		return self.find_element(*self.comment_newstitle)
	def find_commentimgs(self):
		return self.find_elements(*self.comment_img)
	def click_commentimg(self):
		self.find_element(*self.comment_img).click()
		time.sleep(2)
	def find_commenttexts(self):
		return self.find_elements(*self.comment_text)
	def click_commenttext(self):
		self.find_element(*self.comment_text).click()
		time.sleep(1)
	def find_commentreplys(self):
		return self.find_elements(*self.comment_reply)
	def click_commnetreply(self):
		self.find_element(*self.comment_reply).click()
		time.sleep(2)

	def click_commenttitle(self):
		self.find_element(*self.commant_title).click()
		time.sleep(1)
	def click_zantitle(self):
		self.find_element(*self.zan_title).click()
		time.sleep(1)
	def find_inmsgtitle(self):
		return self.find_element(*self.inmsg_title)
	def click_tvcontent(self):
		self.find_element(*self.tv_content).click()
		time.sleep(4)
	def find_tvcontent(self):
		return self.find_element(*self.tv_content)
	def find_tvcontents(self):
		return self.find_elements(*self.tv_content)
	def click_edit(self):
		self.find_element(*self.msg_edit_loc).click()


	def find_msg_titles(self):
		return  self.find_elements(*self.msg_title_loc)


	def find_msg_summarys(self):
		return  self.find_elements(*self.msg_summary_loc)


	def click_selectall(self):
		self.find_element(*self.msg_selectall_loc).click()

	def click_msg_del_button (self):
		self.find_element(*self.msg_del_loc).click()


	def click_els_del(self):
		self.find_element(*self.msg_el_del_loc).click()

	def find_els_msgtitle(self):
		return  self.find_elements(*self.msg_title_loc)
