#coding:utf-8

from apptest.PO import Superunit
from apptest.PO import  MinePage
from apptest.PO import  HisreadPage
from apptest.Public.getmethodname import GetName
from apptest.PO import  NewsPage
from apptest.PO import  InsideNewsPage
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
import os ,time

class hisread(Superunit.initunit):
	work_path=os.path.dirname(os.getcwd())+"\\screen\\historyread\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
	body1=u"我的>历史阅读>UI>未登录>UI检查-空白页"
	def test_01_readUI(self):
		u"""历史阅读UI测试"""
		name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
		MinePage.Mine(self.driver).click_mine_entry()
		MinePage.Mine(self.driver).click_hisred()
		try:
			self.assertTrue(HisreadPage.Hisread(self.driver).find_news_msg())
			self.assertTrue(HisreadPage.Hisread(self.driver).find_clear())
		except:
			print (u"历史阅读>UI>UI检查-空白页")
			filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body1)





