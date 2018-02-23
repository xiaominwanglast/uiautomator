#coding:utf-8

import sys
import time
import os
import unittest
sys.path.append (r"..")

from apptest.PO import nicechoice
from apptest.PO import BasePage
from apptest.PO import SearchPage
from apptest.PO import Superunit
from apptest.Public.getmethodname  import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.PO import channel
from apptest.PO import NewsPage
from apptest.PO import DiscoveryPage
class max(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\subchannel\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_channelmax(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        #首次遍历数组，因为垂直频道只有48个，要额外添加2个，并且还需要1个频道做阀值测试
        channel.channelele(self.driver).click_edit_addchannel()
        mine=channel.channelele(self.driver).allindex()
        print (u"目前我的频道-频道总数%d,需要添加频道数-%d"%(mine[0],50-mine[0]))
        channel.channelele(self.driver).click_channel_back()
        DiscoveryPage.Discovery(self.driver).click_foundentry()
        nicechoice.choose(self.driver).click_choice()
        a=nicechoice.choose(self.driver).find_category()
        count=0
        for i in range(len(a)):
            a[i].click()
            j=nicechoice.choose(self.driver).click_sub(mine[1])
            count=count+j
        print (u"再次添加频道数-%s"%count)
        NewsPage.News(self.driver).click_news_entry()
        channel.channelele(self.driver).click_edit_addchannel()
        for i in range(2):
            BasePage.Base(self.driver).do_swipe(self.driver,"up")
        if count >= 50-mine[0]:
            nowsuggest=channel.channelele(self.driver).sugggestfirst()
            self.driver.find_element_by_name(nowsuggest[0]).click()
            time.sleep(1)
            nextsuggest=channel.channelele(self.driver).sugggestfirst()
            if nextsuggest[0] == nowsuggest[0]:
                print (u"频道阈值为50个，不能再次添加")
            else:
                print (u"频道阈值为50个，任然可以再次添加出现异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"频道阈值为50个，任然可以再次添加出现异常"
                smail().send_errormsg(str(filename),body,self.work_path)
        else:
            print(u"还需要添加频道数为%s"%(50-mine[0]-count))
            num=channel.channelele(self.driver).sugggestfirst()
            for i in range(50-mine[0]-count):
                self.driver.find_element_by_name(num[1][i]).click()
            nowsuggest=channel.channelele(self.driver).sugggestfirst()
            self.driver.find_element_by_name(nowsuggest[0]).click()
            time.sleep(1)
            nextsuggest=channel.channelele(self.driver).sugggestfirst()
            if nextsuggest[0] == nowsuggest[0]:
                print (u"频道阈值为50个，不能再次添加")
            else:
                print (u"频道阈值为50个，任然可以再次添加出现异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"频道阈值为50个，任然可以再次添加出现异常"
                smail().send_errormsg(str(filename),body,self.work_path)


if __name__=="__main__":
    unittest.main()
