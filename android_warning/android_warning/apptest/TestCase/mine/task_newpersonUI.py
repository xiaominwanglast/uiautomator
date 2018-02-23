#coding:utf-8

import random
from apptest.PO import Superunit
from apptest.PO import  TaskCenterPage
from apptest.PO import  BasePage
from apptest.PO import  MinePage
from apptest.PO import  SearchPage
from apptest.Public.getmethodname import GetName
from apptest.PO import  NewsPage
from apptest.PO import  InsideNewsPage
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
import os ,time
from apptest.PO import nicechoice
from apptest.PO import channel
class newPersonUI(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_personUI(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        MinePage.Mine(self.driver).click_task()
        for i in range(2):
            BasePage.Base(self.driver).do_swipe(self.driver,"up")
        try:
            self.assertTrue(TaskCenterPage.taskcenter(self.driver).find_newbangding())
            self.assertTrue(TaskCenterPage.taskcenter(self.driver).find_newperson())
            self.assertTrue(TaskCenterPage.taskcenter(self.driver).find_newrewardback())
        except:
            print (u"我的>任务中心>检查新人专享UI-显示异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"我的>任务中心>检查新人专享UI-显示异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        else:
            try:
                TaskCenterPage.taskcenter(self.driver).click_newbangding()
                self.assertTrue(TaskCenterPage.taskcenter(self.driver).find_newbangding())
                self.driver.back()
                time.sleep(2)
                TaskCenterPage.taskcenter(self.driver).click_newregist()
                self.assertTrue(TaskCenterPage.taskcenter(self.driver).find_newregist())
                self.driver.back()
                time.sleep(2)
                TaskCenterPage.taskcenter(self.driver).click_newfirstshare()
                self.assertTrue(TaskCenterPage.taskcenter(self.driver).find_newfirstshare())
                self.driver.back()
                time.sleep(2)
                TaskCenterPage.taskcenter(self.driver).click_newrewardback()
                self.assertTrue(TaskCenterPage.taskcenter(self.driver).find_newrewardback())
                self.driver.back()
                time.sleep(2)
            except:
                print (u"我的>任务中心>点击绑定账号/注册有礼/首次分享/有奖反馈-显示异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"我的>任务中心>点击绑定账号/注册有礼/首次分享/有奖反馈-显示异常"
                smail().send_errormsg(str(filename),body,self.work_path)
            else:
                name=u"菠萝"
                TaskCenterPage.taskcenter(self.driver).click_newownchannel()
                for i in range(4):
                    BasePage.Base(self.driver).do_swipe(self.driver,"up")
                TaskCenterPage.taskcenter(self.driver).click_newsubchannel()
                nicechoice.choose(self.driver).click_layoutsearch()
                SearchPage.Search(self.driver).input_keywords(name)
                SearchPage.Search(self.driver).click_btn_search()
                try:
                    SearchPage.Search(self.driver).click_subscribe_btn()
                except:
                    pass
                for i in range(3):
                    self.driver.back()
                    time.sleep(2)
                NewsPage.News(self.driver).click_news_entry()
                channel.channelele(self.driver).click_edit_addchannel()
                self.driver.find_element_by_name(name).click()
                try:
                    self.assertTrue(NewsPage.News(self.driver).find_topics())
                except:
                    print (u"我的>任务中心>点击订阅专属频道-显示异常")
                    filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                    body=u"我的>任务中心>点击订阅专属频道-显示异常"
                    smail().send_errormsg(str(filename),body,self.work_path)

    def test_02_removename(self):
        channel.channelele(self.driver).click_edit_addchannel()
        channel.channelele(self.driver).click_edit_channel()
        try:
            self.driver.find_element(u"菠萝").click()
            time.sleep(1)
        except:
            pass
        channel.channelele(self.driver).click_edit_channel()
        self.driver.back()
