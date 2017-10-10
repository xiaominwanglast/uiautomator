#coding:utf-8
import smtplib
from email.mime.text import MIMEText
import time
def mal():
    with open('gggg.txt','rb') as fs:
        body=fs.read()
    msg = MIMEText(body,'html', 'utf-8')
    msg["Subject"] = u"[%s]每日积分任务"%time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    msg["From"]    = "1727500963@qq.com"
    msg["To"]      = ','.join(['2274052689@qq.com'])
    try:
        s = smtplib.SMTP_SSL('smtp.qq.com',465)
        s.login("1727500963@qq.com","cxbobmaclmejjfgc")
        s.sendmail("1727500963@qq.com", msg["To"], msg.as_string())
        s.quit()
        print "Success!"
    except smtplib.SMTPException,e:
        print "sendemail_Falied,the reson is %s"%e
log_path='C:\\Users\\Administrator\\Desktop\\jifen\\log.txt'
with open('gggg.txt','wb') as fs:
    data=u''
    fs.write(data.encode('utf-8'))
mal()