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
from appium.webdriver.common.touch_action import TouchAction
from apptest.PO.channel import channelele
from apptest.PO import SearchPage
from apptest.PO import NewsPage

#新闻频道管理>删除频道
#1.新闻>右上角“+”进入频道管理＞我的频道>长按除了头条和滚动以外的任意频道
#2.新闻>右上角“+”进入频道管理＞我的频道>点击编辑按钮
#3.选择除了头条和滚动以外的垂直频道>点删除图标（X）
#4.选择除了头条和滚动以外的自定义频道>点删除图标（X）
#5.点击返回按钮，查看频道列表

class nologin_channeldelete(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\channel\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_editAnyChannel(self):
        #我的频道>点击编辑按钮
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        channel.channelele(self.driver).click_edit_addchannel()
        countBefore=channelele(self.driver).allindex()
        print (u"编辑前我的频道总数：%d"%countBefore[0])
        channel.channelele(self.driver).click_edit_channel()
        channel.channelele(self.driver).click_indexone(0)
        self.allDelete=channel.channelele(self.driver).find_channel_delete()
        try:
            self.driver.find_element_by_name(u"头条")
            self.assertEqual(countBefore[0]-1,len(self.allDelete))
            print (u"头条未删除正常")
        except:
            print(u"频道删除出现异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"频道删除出现异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        channel.channelele(self.driver).click_edit_channel()

    def test_02_longClickChannel(self):
        #我的频道>长按除了头条和滚动以外的任意频道
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        channel.channelele(self.driver).click_edit_addchannel()
        countBefore=channelele(self.driver).allindex()
        print (u"编辑前我的频道总数：%d"%countBefore[0])
        a=random.randint(1,countBefore[0]-1)
        longClick=channel.channelele(self.driver).indexone(a)
        TouchAction(self.driver).press(longClick).wait(2000).perform()
        channel.channelele(self.driver).click_indexone(0)
        self.allDelete=channel.channelele(self.driver).find_channel_delete()
        try:
            self.driver.find_element_by_name(u"头条")
            self.assertEqual(countBefore[0]-1,len(self.allDelete))
            print (u"头条未删除正常")
        except:
            print(u"频道删除出现异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"频道删除出现异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        channel.channelele(self.driver).click_edit_channel()

    def test_03_deleteX(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        channel.channelele(self.driver).click_edit_addchannel()
        countBefore=channelele(self.driver).allindex()
        listone=channel.channelele(self.driver).allchannel(countBefore[1])
        a=random.randint(0,len(listone[0])-1)
        channel.channelele(self.driver).click_edit_channel()
        name=listone[0][a]
        print (u"点击删除的垂直频道是%s"%name)
        self.driver.find_element_by_name(name).click()
        channel.channelele(self.driver).click_edit_channel()
        countnext=channelele(self.driver).allindex()
        try:
            self.assertTrue(name not in countnext[1])
            self.assertEqual(name,countnext[3][0])
        except:
            print(u"删除垂直频道出现异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"删除垂直频道出现异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        else:
            self.driver.find_element_by_name(name).click()
            try:
                self.assertFalse(NewsPage.News(self.driver).find_topics())
            except:
                print(u"删除垂直频道返回查看出现异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"删除垂直频道返回查看出现异常"
                smail().send_errormsg(str(filename),body,self.work_path)

    def test_04_deleteY(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        channel.channelele(self.driver).click_edit_addchannel()
        countBefore=channel.channelele(self.driver).allindex()
        onelist=channel.channelele(self.driver).allchannel(countBefore[1])
        if(onelist[1]):
            onechannel=onelist[1][0]
            number=onelist[2]
        else:
            #添加一个自定义频道
            onechannel='lol'
            number=2
            print (u"新安装的app无自定义频道，需添加一个自定义频道-%s"%onechannel)
            channel.channelele(self.driver).click_channel_back()
            SearchPage.Search(self.driver).click_entry()
            SearchPage.Search(self.driver).input_keywords(onechannel)
            SearchPage.Search(self.driver).click_btn_search()
            SearchPage.Search(self.driver).click_subscribe_btn()
            print (u"已订阅一个频道：%s"%onechannel)
            NewsPage.News(self.driver).click_news_entry()
            channel.channelele(self.driver).click_edit_addchannel()
        channel.channelele(self.driver).click_edit_channel()
        channel.channelele(self.driver).click_indexone(number)
        channel.channelele(self.driver).click_edit_channel()
        print (u"删除自定义频道-%s"%onechannel)
        #删除后开始遍历我的频道元素
        countNext=channelele(self.driver).allindex()
        try:
            self.assertTrue(onechannel not in countNext[1])
            self.assertTrue(onechannel not in countNext[3])
        except:
            print(u"删除自定义频道出现异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body1=u"删除自定义频道出现异常"
            smail().send_errormsg(str(filename),body1,self.work_path)
        else:
            channel.channelele(self.driver).click_channel_back()
            for x in range(0,number):
                Base(self.driver).do_swipe(self.driver,"left")
            time.sleep(3)
            select=channel.channelele(self.driver).select_channel()
            if (onechannel != select):
                pass
            else:
                print(u"删除自定义频道返回后仍然存在，出现异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body3=u"删除自定义频道返回后仍然存在，出现异常"
                smail().send_errormsg(str(filename),body3,self.work_path)

if __name__=="__main__":
    unittest.main()
