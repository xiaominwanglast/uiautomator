#coding:utf-8

from apptest.PO import Superunit
from apptest.PO import MinePage
from apptest.Public.getmethodname import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.PO import NewsPage
import os ,time
from apptest.PO import CollectPage
from apptest.PO import VideoPage
from apptest.PO.adbUtils import ADB
class collectother(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_collectA(self):
        name1=self.__class__.__name__ +'.'+GetName.get_current_function_name()
        NewsPage.News(self.driver).click_topic()
        CollectPage.Collect(self.driver).click_save_page()
        self.driver.back()
        VideoPage.Video(self.driver).click_video_entry()
        VideoPage.Video(self.driver).click_save()
        MinePage.Mine(self.driver).click_mine_entry()
        CollectPage.Collect(self.driver).click_mine_collect()
        self.driver.back()
    def test_02_clearAppdata(self):
        MinePage.Mine(self.driver).click_mine_entry()
        print (u"清理缓存数据")
        ADB().clearAppData(ADB().getCurrentPackageName())

    def test_03_collectB(self):
        name1=self.__class__.__name__ +'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        CollectPage.Collect(self.driver).click_mine_collect()
        CollectPage.Collect(self.driver).click_tv_text()
        try:
            self.assertFalse(CollectPage.Collect(self.driver).find_topics())
            CollectPage.Collect(self.driver).click_tv_video()
            self.assertFalse(CollectPage.Collect(self.driver).find_videotitles())
        except:
            print (u"收藏>本地收藏-未登录不同设备收藏不同-出现异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"收藏>本地收藏-未登录不同设备收藏不同-出现异常"
            smail().send_errormsg(str(filename),body,self.work_path)
