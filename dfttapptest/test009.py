#coding:utf-8
import smtplib
from email.mime.text import MIMEText
_user = "1727500963@qq.com"
_pwd  = "cxbobmaclmejjfgc"#zetwuqfcdxetdijc
_to   = ['wangxiaomin@021.com','2274052689@qq.com']

msg = MIMEText(u'哈哈','html', 'utf-8')
msg["Subject"] = "don't panic"
msg["From"]    = _user
msg["To"]      =','.join(_to)

try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, msg["To"], msg.as_string())
    s.quit()
    print "Success!"
except smtplib.SMTPException,e:
    print "Falied,%s"%e