#coding:utf-8
from apptest.PO import Superunit
from apptest.PO import  MinePage
from apptest.Public.getmethodname import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
import os ,time
from apptest.PO import  MsgPage

class mesg(Superunit.initunit):
	work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\mesg\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
	body1=u"我的>消息中心>UI>未登录>UI检查-空白页"
	def test_01_newmsg(self):
		u"""消息中心UI测试"""
		name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
		MinePage.Mine(self.driver).click_mine_entry()
		MinePage.Mine(self.driver).click_msg()
		try:
			self.assertTrue(MsgPage.Msg(self.driver).find_tvtitles())
		except:
			print (u"消息中心>UI>UI检查-空白页")
			filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body1)



