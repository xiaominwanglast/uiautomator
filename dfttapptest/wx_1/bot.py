#!/usr/bin/env python
# coding: utf-8

from wxbot import *
import threading
from login_tower import deal_tower_data
from score import *
from tianqi_2345 import succesion
import json
from douban import douban

class TulingWXBot(WXBot):
    def __init__(self):
        WXBot.__init__(self)
        self.path= os.path.dirname(os.getcwd())+'\\wx_1\\data\\'+u'东方头条_自动化.txt'
     #   self.path1= os.path.dirname(os.getcwd())+'\\wx_1\\data\\'+u'天气快报_自动化.txt'
        self.num=0
        self.limit_sch1=[]
        self.limit_sch2=[]
        self.group_name=[]
        self.tuling_key = "e5ccc9c7c8834ec3b08940e290ff1559"
        self.robot_switch = True
        '''
        try:
            cf = ConfigParser.ConfigParser()
            cf.read('conf.ini')
            self.tuling_key = cf.get('main', 'key')
        except Exception:
            pass
        '''
 #       print 'tuling_key:', self.tuling_key

    def tuling_auto_reply(self, uid, msg):
        if self.tuling_key:
            url = "http://www.tuling123.com/openapi/api"
            user_id = uid.replace('@', '')[:30]
            body = {'key': self.tuling_key, 'info': msg.encode('utf8'), 'userid': user_id}
            r = requests.post(url, data=body)
            respond = json.loads(r.text)
            result = ''
            if respond['code'] == 100000:
                result = respond['text'].replace('<br>', '  ')
                result = result.replace(u'\xa0', u' ')
            elif respond['code'] == 200000:
                result = respond['url']
            elif respond['code'] == 302000:
                for k in respond['list']:
                    result = result + u"【" + k['source'] + u"】 " +\
                        k['article'] + "\t" + k['detailurl'] + "\n"
            else:
                result = respond['text'].replace('<br>', '  ')
                result = result.replace(u'\xa0', u' ')
            print '    ROBOT:', result
            return result
        else:
            return u"知道啦"

    def auto_switch(self, msg):
        msg_data = msg['content']['data']
        stop_cmd = [u'退下', u'走开', u'关闭', u'关掉', u'休息', u'滚开',u'结束']
        start_cmd = [u'开启']
        if self.robot_switch:
            for i in stop_cmd:
                if i == msg_data:
                    self.robot_switch = False
                    self.send_msg_by_uid(u'[机器]' + u'机器人已关闭！', msg['to_user_id'])
            for i in start_cmd:
                if i == msg_data:
                #    print msg['to_user_id']
                    #根据i出现次数来分配group_name,同时对group_name进行判断是否一致，然后根据time.time()判断分配时间顺序
                    if self.num==0:
                        self.send_msg_by_uid(u'[机器]' + u'机器人开启！', msg['to_user_id'])
                   #     self.send_msg_by_uid(u'[机器]' + u'本群监测自动化', msg['to_user_id'])
                        self.group_name.append(msg['to_user_id'])
                        self.num+=1
                    '''
                    elif self.num==1 and self.group_name[0]!=msg['to_user_id']:
                        self.group_name.append(msg['to_user_id'])
                        self.send_msg_by_uid(u'[机器]' + u'机器人开启！', msg['to_user_id'])
                        self.send_msg_by_uid(u'[机器]' + u'本群计划推送信息', msg['to_user_id'])
                        self.num+=1
                    '''
        else:
            for i in start_cmd:
                if i == msg_data:
                    self.robot_switch = True
                    self.send_msg_by_uid(u'[机器]' + u'机器人已开启！', msg['to_user_id'])


    def handle_msg_all(self, msg):
        if not self.robot_switch and msg['msg_type_id'] != 1:
            return
        if msg['msg_type_id'] == 1 and msg['content']['type'] == 0 :  # reply to self
            self.auto_switch(msg)
        elif msg['msg_type_id'] == 4 and msg['content']['type'] == 0:  # text message from contact
         #   self.send_msg_by_uid(u'url数据已保存', msg['user']['id'])
            self.send_msg_by_uid(u'[图灵]' +self.tuling_auto_reply(msg['user']['id'], msg['content']['data']), msg['user']['id'])
        elif msg['msg_type_id'] == 3 and msg['content']['type'] == 0:  # group text message
            if 'detail' in msg['content']:
                my_names = self.get_group_member_name(msg['user']['id'], self.my_account['UserName'])
                if my_names is None:
                    my_names = {}
                if 'NickName' in self.my_account and self.my_account['NickName']:
                    my_names['nickname2'] = self.my_account['NickName']
                if 'RemarkName' in self.my_account and self.my_account['RemarkName']:
                    my_names['remark_name2'] = self.my_account['RemarkName']
                is_at_me = False
                for detail in msg['content']['detail']:
                    if detail['type'] == 'at':
                        for k in my_names:
                            if my_names[k] and my_names[k] == detail['value']:
                                is_at_me = True
                                break
                if is_at_me:
                    src_name = msg['content']['user']['name']
                    reply = '@' + src_name + ': '
                    if msg['content']['type'] == 0:  # text message
                        if u'积分'in msg['content']['data'] and do_data():
                            self.send_msg_by_uid(do_data(), msg['user']['id'])
                        elif u'电影' in msg['content']['data'] and douban():
                            self.send_msg_by_uid(douban(), msg['user']['id'])
                        else:
                            reply += self.tuling_auto_reply(msg['content']['user']['id'], msg['content']['desc'])
                            self.send_msg_by_uid(u'[图灵]'+reply, msg['user']['id'])
                    else:
                        reply += u"sorry,不识别字体O(∩_∩)O哈哈~"
                        self.send_msg_by_uid(u'[机器]'+reply, msg['user']['id'])
    #计划任务,加入特殊判断
    def schedule(self):
        #涉及到多线程，暂时未加入，阻塞时间过长，不确定会触发问题。
        if os.path.exists(self.path):
            with open(self.path,'rb') as fs:
                text=fs.read()
            try:
                if text!='':
                    self.send_msg_by_uid(u'[自动化]'+text.decode('gbk'),self.group_name[0])
                    os.remove(self.path)
            except:
                pass
        '''
        if os.path.exists(self.path1):
            with open(self.path1,'rb') as fs:
                text1=fs.read()
            try:
                if text1!='':
                    self.send_msg_by_uid(text1.decode('gbk'),self.group_name[1])
                    os.remove(self.path1)
            except:
                pass
        '''
        #定时任务，参数最后时间进行清0
        try:
            #限于小时_分钟
            sch=time.strftime('%H_%M', time.localtime(time.time()))
            #限于每周,周几
            #sch1=time.strftime('%w')
            '''
            if sch=='08_20':
                if deal_tower_data():
                    self.limit_sch1.append(deal_tower_data())
                    self.send_msg_by_uid(self.limit_sch1.pop(),self.group_name[0])
            '''
            if sch=='09_47':
                if succesion():
                    self.limit_sch2.append(succesion())
                    self.send_msg_by_uid(self.limit_sch2.pop(),self.group_name[0])
        except:
            pass


def main():
    bot = TulingWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()


if __name__ == '__main__':
    main()

