#!/usr/bin/env python
# coding: utf-8
#
import xlrd
from wxbot import *
import os
from xlutils.copy import copy
class MyWXBot(WXBot):
    def __init__(self):
        WXBot.__init__(self)
        self.Test_url=[]
        self.num=0
        self.work_path=os.path.dirname(os.getcwd())+'\\wx_1\\Test_url.xls'
        self.result_path=os.path.dirname(os.getcwd())+'\\wx_1\\Test_Url_Result.xls'
        wk=xlrd.open_workbook(self.work_path)
        sheet=wk.sheet_by_name('Sheet1')
        for i in range(1,sheet.nrows):
            self.Test_url.append((sheet.cell_value(i,0)+sheet.cell_value(i,1)+sheet.cell_value(i,2)).strip())
    def handle_msg_all(self, msg):
        pass
      #  if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
       #     self.send_msg_by_uid(u'hi', msg['user']['id'])
            #self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
            #self.send_file_msg_by_uid("img/1.png", msg['user']['id'])

    def schedule(self):
        url_data=self.Test_url.pop()
        print url_data
        self.send_msg(u'auto', url_data)
        wp=xlrd.open_workbook(self.result_path)
        sheet=wp.sheet_by_name('Sheet1')
        cp=copy(wp)
        cp.get_sheet(0).write(sheet.nrows,0,url_data)
        cp.save(self.result_path)
        if self.num==0:
            time.sleep(80)
        else:
            time.sleep(30)
        self.num+=1

def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()

if __name__ == '__main__':
    main()

