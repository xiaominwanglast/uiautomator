#coding:utf-8


from apptest.PO import Superunit
from apptest.PO import  MinePage
from apptest.Public.getmethodname import GetName
from apptest.PO import  BasePage
from apptest.PO import  InsideNewsPage
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
import os ,time
from apptest.PO import  TaskCenterPage
from apptest.PO import  PursePage
from apptest.PO import  SetPage
from apptest.PO import  OfflinePage
import random
from selenium.webdriver.support.ui import WebDriverWait
import unittest

class  clear(Superunit.initunit):

	work_path=os.path.dirname(os.getcwd())+"\\screen\\clearcache\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
	def test_01_clear(self):
		name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
		MinePage.Mine(self.driver).click_mine_entry()
		MinePage.Mine(self.driver).click_set()
		#先点击取消，后面再点击确定按钮
		SetPage.Set(self.driver).click_clear()
		SetPage.Set(self.driver).click_clear_cancle()
		SetPage.Set(self.driver).click_clear()
		SetPage.Set(self.driver).click_clear_ok()
		getsizestr=SetPage.Set(self.driver).get_el_size()
		if getsizestr=="0M":
			print (u"清除缓存成功")
		else:
			print (u"清除缓存不成功")
			filename=screenshot().screencap(self.work_path,self.driver,name=name1)
			body=u"清除缓存不成功"
			smail().send_errormsg(str(filename),body,self.work_path)



	def test_02_delpage(self):
		#先进行离线下载操作，然后判断离线下载的内容是否正常清空了
		name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
		MinePage.Mine(self.driver).click_mine_entry()
		BasePage.Base(self.driver).do_swipe(self.driver,"up")
		MinePage.Mine(self.driver).click_offline()
		#点击下载按钮来进行下载操作
		OfflinePage.page(self.driver).click_downloadid()
		OfflinePage.page(self.driver).find_switch_buttons()[0].click()
		dlnum=random.randint(1,len(OfflinePage.page(self.driver).find_switch_buttons())-1)
		OfflinePage.page(self.driver).find_switch_buttons()[dlnum].click()
		OfflinePage.page(self.driver).click_dlbutton()
		try:
			self.driver.find_element_by_name(u"取消离线")
		except:
			print (u"第一次没有下载成功")
			OfflinePage.page(self.driver).find_switch_buttons()[dlnum].click()
			OfflinePage.page(self.driver).click_dlbutton()
		time.sleep(30)
		for i in range(6):
			try:
				self.driver.find_element_by_name(u"开始离线")
				break
			except:
				time.sleep(30)
		self.driver.back()
		self.driver.back()
		BasePage.Base(self.driver).do_swipe(self.driver,"down")
		MinePage.Mine(self.driver).click_set()
		SetPage.Set(self.driver).click_clear()
		SetPage.Set(self.driver).click_clear_ok()
		self.driver.back()
		BasePage.Base(self.driver).do_swipe(self.driver,"up")
		MinePage.Mine(self.driver).click_offline()
		try:
			self.assertFalse(OfflinePage.page(self.driver).find_dlpage_els())
		except:
			print (u"清除缓存失败")
			filename=screenshot().screencap(self.work_path,self.driver,name=name1)
			body=u"清除缓存功能失败"
			smail().send_errormsg(str(filename),body,self.work_path)


if __name__=="__main__":
	unittest.main()