#coding:utf-8

import sys
import time
import os
import unittest
sys.path.append (r"..")

from apptest.PO import nicechoice
from apptest.PO import SearchPage
from apptest.PO import Superunit
from apptest.Public.getmethodname  import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.PO import channel
from apptest.PO import NewsPage


class sub_indexteams(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\subchannel\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_indexteams(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        name=u"李"
        NewsPage.News(self.driver).click_news_entry()
        channel.channelele(self.driver).click_edit_addchannel()
        channel.channelele(self.driver).click_add_channel()
        nicechoice.choose(self.driver).click_layoutsearch()
        SearchPage.Search(self.driver).input_keywords(name)
        try:
            self.assertTrue(nicechoice.choose(self.driver).find_textone())
            e=nicechoice.choose(self.driver).find_texttitle()
        except:
            print (u"输入搜索词时显示异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"输入搜索词时显示异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        else:
            print (u"点击订阅%s"%e[0].text)
            e[0].click()
            time.sleep(3)
            nicechoice.choose(self.driver).click_subscribe()
            for i in range(3):
                channel.channelele(self.driver).click_backleft()
            channel.channelele(self.driver).click_edit_channel()
            channel.channelele(self.driver).click_indexone(2)
            channel.channelele(self.driver).click_edit_channel()

if __name__=="__main__":
    unittest.main()