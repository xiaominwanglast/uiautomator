#coding:utf-8
import random
import sys
import time
import os
import unittest
sys.path.append (r"..")
from random import choice

from apptest.PO import Superunit
from apptest.Public.getmethodname  import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.PO import NewsPage
from apptest.PO import BasePage
from apptest.PO import channel
from apptest.PO import SearchPage
from apptest.PO.BasePage import Base
#新闻内页>新闻我要报错
#1.新闻>信息流>频道（随机取）>点击任意新闻标题>进入新闻内页，点击【我要报错】按钮
#2.选择报错原因（单选或多选）或输入框内输入投诉或纠错的内容>点击提交

class nologin_feedback(Superunit.initunit):
    work_path = os.path.dirname(os.getcwd())+"\\screen\\nologin\\news\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_feedback(self):
        name1=self.__class__.__name__ +'.'+GetName.get_current_function_name()
        channel.channelele(self.driver).click_edit_addchannel()
        mine=channel.channelele(self.driver).allindex()
        chan=choice(mine[1])
        print(u"随机选择我的频道-%s"%chan)
        self.driver.find_element_by_name("%s"%chan).click()
        time.sleep(3)
        NewsPage.News(self.driver).click_topic()
        print (u"--------正在查找我要报错---------")
        for i in range(80):
            try:
       #         self.assertTrue(NewsPage.News(self.driver).find_feedback())
                self.driver.find_element_by_id("%s:id/tv_feedback_error"%Base.capabilities['appPackage'])
                break
            except:
                BasePage.Base(self.driver).do_swipe(self.driver,"bigup")
        NewsPage.News(self.driver).click_feedback()
        try:
            self.assertTrue(NewsPage.News(self.driver).find_titletext())
            self.assertTrue(NewsPage.News(self.driver).find_textcontent())
            BasePage.Base(self.driver).do_swipe(self.driver,"up")
            self.assertTrue(NewsPage.News(self.driver).find_textcontent())
            self.assertTrue(NewsPage.News(self.driver).find_commit())

        except:
            print (u"点开新闻内页我要报错显示异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body1=u"点开新闻内页我要报错显示异常"
            smail().send_errormsg(str(filename),body1,self.work_path)
        else:
            e1=NewsPage.News(self.driver).find_textcontent()
            e1[0].click()
            NewsPage.News(self.driver).click_commit()
            try:
                self.assertTrue(NewsPage.News(self.driver).find_feedback())
            except:
                print (u"我要报错-提交一个选项后返回显示异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body2=u"我要报错-提交一个选项后返回显示异常"
                smail().send_errormsg(str(filename),body2,self.work_path)
            else:
                NewsPage.News(self.driver).click_feedback()
                BasePage.Base(self.driver).do_swipe(self.driver,"up")
                e1=NewsPage.News(self.driver).find_textcontent()
                e1[0].click()
                e1[2].click()
                NewsPage.News(self.driver).click_commit()
                try:
                    self.assertTrue(NewsPage.News(self.driver).find_feedback())
                except:
                    print (u"我要报错-提交多个选项后返回显示异常")
                    filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                    body3=u"我要报错-提交多个选项后返回显示异常"
                    smail().send_errormsg(str(filename),body3,self.work_path)
                else:
                    NewsPage.News(self.driver).click_feedback()
                    BasePage.Base(self.driver).do_swipe(self.driver,"up")
                    e1=NewsPage.News(self.driver).find_textcontent()
                    e1[0].click()
                    NewsPage.News(self.driver).click_edit(u"辣眼睛")
                    NewsPage.News(self.driver).click_commit()
                    try:
                        self.assertTrue(NewsPage.News(self.driver).find_feedback())
                    except:
                        print (u"我要报错-提交投诉或是纠错内容后返回显示异常")
                        filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                        body5=u"我要报错-提交投诉或是纠错内容后返回显示异常"
                        smail().send_errormsg(str(filename),body5,self.work_path)
                    else:
                        print (u"新闻内页-我要报错-测试通过")

if __name__=="__main__":
    unittest.main()




