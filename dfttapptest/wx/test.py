#!/usr/bin/env python
# coding: utf-8
#
from score import *
from wxbot import *
class MyWXBot(WXBot):
    def tuling_auto_reply(self, uid, msg):
        self.tuling_key="e5ccc9c7c8834ec3b08940e290ff1559"
        if self.tuling_key:
            url = "http://www.tuling123.com/openapi/api"
            user_id = uid.replace('@', '')[:30]
            body = {'key': self.tuling_key, 'info': msg.encode('utf8'), 'userid': user_id}
            r = requests.post(url, data=body)
            respond = json.loads(r.text)
            if respond['code'] == 100000:
                result = respond['text'].replace('<br>', '  ')
            elif respond['code'] == 200000:
                result = respond['url']
            else:
                result = respond['text'].replace('<br>', '  ')
            return result
        else:
            return u"知道啦"
    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            if u'积分'in msg['content']['data']:
                self.send_msg_by_uid(do_data(), msg['user']['id'])
            else:
                self.send_msg_by_uid(self.tuling_auto_reply(msg['user']['id'], msg['content']['data']), msg['user']['id'])
         #   self.send_msg_by_uid(u'hi', msg['user']['id'])
         #   self.send_img_msg_by_uid(r"E:\wxm\pycharm\python\kuaibao_android_GUI\apptest\screen\login\activity\2017-03-12\screen.png", msg['user']['id'])
            #self.send_file_msg_by_uid("img/1.png", msg['user']['id'])
        '''
        if msg['msg_type_id']==3:
            if msg['content']['data'].find('@') >= 0:  # someone @ another
                print msg['user']['id']
                my_names = self.get_group_member_name(msg['user']['id'], self.user['NickName'])
                print my_names
                if my_names is None:
                    my_names = {}
                if 'NickName' in self.user and len(self.user['NickName']) > 0:
                    my_names['nickname2'] = self.user['NickName']
                if 'RemarkName' in self.user and len(self.user['RemarkName']) > 0:
                    my_names['remark_name2'] = self.user['RemarkName']
                is_at_me = False
                text_msg = ''
                for _ in my_names:
                    if msg['content']['data'].find('@'+my_names[_]) >= 0:
                        is_at_me = True
                        text_msg = msg['content']['data'].replace('@'+my_names[_], '').strip()
                        break
                if is_at_me:  # someone @ me
                    snames = self.get_group_member_name(msg['user']['id'], msg['content']['user']['id'])
                    src_name = ''
                    if 'display_name' in snames:
                        src_name = snames['display_name']
                    elif 'nickname' in snames:
                        src_name = snames['nickname']
                    elif 'remark_name' in snames:
                        src_name = snames['remark_name']
                    if src_name != '':
                        reply = '@' + src_name + ' '
                        if msg['content']['type'] == 0:  # text message
                            reply += self.tuling_auto_reply(msg['content']['user']['id'], text_msg)
                        else:
                            reply += u"对不起，只认字，其他杂七杂八的我都不认识，,,Ծ‸Ծ,,"
                        self.send_msg_by_uid(reply, msg['user']['id'])
    def schedule(self):
      #  self.send_msg(u'大学_李玉龙', u'测试')
        scheduler = BlockingScheduler()
        scheduler.add_job(do_run(),'cron',hour=16,minute=20)

def do_run():
    WXBot().send_msg(u'头条_观文', u'计划测试')
'''


def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()
if __name__ == '__main__':
    main()
