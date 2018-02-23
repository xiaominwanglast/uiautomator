#coding:utf-8


from apptest.PO import Superunit
from apptest.PO import  MinePage
from apptest.Public.getmethodname import GetName
from apptest.PO import  NewsPage
from apptest.PO import  InsideNewsPage
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
import os ,time
from apptest.PO import  TaskCenterPage
from apptest.PO import  PursePage


class  signed(Superunit.initunit):

	work_path=os.path.dirname(os.getcwd())+"\\screen\\sign\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

	def test_01_signjude(self):
		name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
		MinePage.Mine(self.driver).click_mine_entry()
		MinePage.Mine(self.driver).click_task()
		#获取签到的天数
		signdays=TaskCenterPage.taskcenter(self.driver).find_sign_ele()[6]
		self.driver.back()
		MinePage.Mine(self.driver).click_purse()
		#获取现在的总积分
		nosignbonus=PursePage.purse(self.driver).find_login_total_bonus()
		self.driver.back()
		#执行签到操作
		NewsPage.News(self.driver).click_news_entry()
		try:
			NewsPage.News(self.driver).click_sign()
		except:
			print (u"已经签到或者网络不通")
		else:
			#计算签到后的积分是否正确
			MinePage.Mine(self.driver).click_mine_entry()

			MinePage.Mine(self.driver).click_purse()
			signedbonus=PursePage.purse(self.driver).find_login_total_bonus()
			if int(signdays)!=6:
				if int(signedbonus)-int(nosignbonus)==int(signdays)+1:
					print u"签到积分正确"
				else:
					print u"签到积分不正确"
			else:
				if int(signedbonus)-int(nosignbonus)>7:
					print u"已经连续签到7天，并成功获取到礼包奖励积分%s"%(int(signedbonus)-int(nosignbonus)-7)
				else:
					print u"未获取到连续签到奖励积分"
					filename=screenshot().screencap(self.work_path,self.driver,name=name1)
					body=u"任务中心签到界面异常"
					smail().send_errormsg(str(filename),body,self.work_path)


	def test_02_sign(self):
		name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
		print name1
		MinePage.Mine(self.driver).click_mine_entry()
		MinePage.Mine(self.driver).click_task()

		try:
			el=TaskCenterPage.taskcenter(self.driver).find_login_el()
			if el.get_attribute('name')==u"签到":
				el.click()
				print u"签到成功"
			else:
				el.get_attribute('name')==u"未登录"
				print u"账号未登录"
		except:
			try:
				integral=TaskCenterPage.taskcenter(self.driver).find_signtoday_el()
				print u"今天已经签到%s" %integral
			except:
				print u"任务中心签到界面异常"
				filename=screenshot().screencap(self.work_path,self.driver,name=name1)
				body=u"任务中心签到界面异常"
				smail().send_errormsg(str(filename),body,self.work_path)