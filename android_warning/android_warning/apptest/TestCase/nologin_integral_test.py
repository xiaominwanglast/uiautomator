#coding:utf-8

import random
from apptest.PO import Superunit
from apptest.PO import  MinePage
from apptest.Public.getmethodname import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.PO import PursePage
import os ,time

class  nologin_points(Superunit.initunit):
		work_path=os.path.dirname(os.getcwd())+"\\screen\\integral\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

		def test_01_jude(self):
			name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
			print name1

			bonus=0
			MinePage.Mine(self.driver).click_mine_entry()
			MinePage.Mine(self.driver).click_purse()
			try:
				time.sleep(2)
				if (PursePage.purse(self.driver).find_login_total_bonus()):
					time.sleep(1)
					bonus=PursePage.purse(self.driver).find_login_total_bonus()
			except:
				bonus='0'
			if int(bonus)==0:
				print (u"账号积分为0可能未登录")
			self.driver.back()
			MinePage.Mine(self.driver).click_mall()
			time.sleep(10)
			try:
				self.driver.find_element_by_name(u"可用积分：%s"%bonus)
			except:
				print (u"钱包的积分和商城的积分不相同")
				filename=screenshot().screencap(self.work_path,self.driver,name=name1)
				body1=u"钱包的积分和商城的积分不相同"
				smail().send_errormsg(str(filename),body1,self.work_path)
