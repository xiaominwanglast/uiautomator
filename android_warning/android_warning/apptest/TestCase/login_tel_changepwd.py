#coding:utf-8

import sys
import time
import os

sys.path.append (r"..")

from apptest.PO import BasePage
from apptest.PO import MinePage
from apptest.PO import Superunit
from apptest.PO import CollectPage
from apptest.PO import SetPage
from apptest.Public.getmethodname  import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail

class changepassword(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\login\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_changepwd(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        BasePage.Base(self.driver).do_swipe(self.driver,"up")
        MinePage.Mine(self.driver).click_set()
        SetPage.Set(self.driver).click_changepwd()

