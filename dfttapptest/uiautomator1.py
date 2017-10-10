#coding:utf-8
import time
from uiautomator import Device
d = Device('F8UDU15214030172')
d.press.home()
d(text=u'广东头条').click()
time.sleep(5)
d(text=u'广东').click()
time.sleep(3)
d.click(320,900)
time.sleep(3)
d(text=u'写评论,得积分!').click()
d(text=u'优质评论将会被优先展示').set_text(u"1111")
time.sleep(3)

d.press.back()
d.press.home()