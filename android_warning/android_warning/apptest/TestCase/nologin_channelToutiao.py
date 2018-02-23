#coding:utf-8
import random
import sys
import time
import os
import unittest
sys.path.append (r"..")


from apptest.PO import channel
from apptest.PO import Superunit
from apptest.Public.getmethodname  import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.PO.BasePage import Base


#新闻频道>频道显示，
# 1.固定频道【头条】位于首位，总频道数目不超过50个
#频道总数低于50个，这条后期再改

class nologin_channeltoutiao(Superunit.initunit):
    work_path = os.path.dirname(os.getcwd())+"\\screen\\nologin\\channel\\toutiao\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_toutiao(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        channel.channelele(self.driver).click_news_enter()
        time.sleep(5)
        e1=(channel.channelele(self.driver).find_channel_tv())[0:5]
        if (e1[0].text !=u"头条"):
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"新闻频道第一条不是头条"
            smail().send_errormsg(str(filename),body,self.work_path)
        else:
            print (u"新闻频道第一条是头条")
        #频道总数不超过50位
        channel.channelele(self.driver).click_edit_addchannel()
        channelcount=channel.channelele(self.driver).allindex()
        print (u"频道管理-我的频道总数是：%d"%channelcount[0])
        if(channelcount[0]<=50):
            pass
        else:
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"频道管理频道总数超过50出现异常"
            smail().send_errormsg(str(filename),body,self.work_path)
if __name__=="__main__":
    unittest.main()