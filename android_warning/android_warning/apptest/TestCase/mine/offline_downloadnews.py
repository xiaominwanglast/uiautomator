#coding:utf-8

import unittest
from apptest.PO import  MinePage
from apptest.PO import Superunit
from apptest.PO import  BasePage
from apptest.PO import  OfflinePage
from apptest.Public.getmethodname import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
import os ,time

class dlnews(Superunit.initunit):
	work_path=os.path.dirname(os.getcwd())+"\\screen\\offline\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
	body1=u"我的>离线阅读>UI>未登录>UI检查-空白页"
	def test_01_UItest(self):
		u"""离线阅读UI测试"""
		name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
		MinePage.Mine(self.driver).click_mine_entry()
		BasePage.Base(self.driver).do_swipe(self.driver,"up")
		time.sleep(5)
	#	MinePage.Mine(self.driver).click_offline()
		self.driver.find_element_by_id('com.songheng.eastnews:id/rl_download_mode').click()
		time.sleep(2)
		OfflinePage.page(self.driver).click_downloadid()
		try:
			self.assertTrue(OfflinePage.page(self.driver).find_dlclickloc())
		except:
			print (u"离线阅读>UI>UI检查-空白页")
			filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body1)


if __name__=="__main__":
	unittest.main()