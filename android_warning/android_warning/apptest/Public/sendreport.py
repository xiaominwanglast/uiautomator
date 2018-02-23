# -*- coding: UTF-8 -*-

import smtplib
from email.utils import formatdate
from email.header import Header
from email import encoders
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
from email.mime.base import MIMEBase
import time
import ConfigParser
import os
from apptest.Public import readconfig

def readmsg():
    config = ConfigParser.ConfigParser()

    filejudge=os.path.dirname(os.getcwd())
    while True:
        if os.path.exists(filejudge+"\\config\\config.ini"):
            break
        else:
            filejudge=os.path.dirname(filejudge)

    with open(filejudge+"\\config\\config.ini","r") as cfgfile:
        config.readfp(cfgfile)
        smtpHost=config.get("email","smtpHost")
        smtpPort=config.get("email","smtpPort")
        sslPort=config.get("email","sslPort")
        fromMail=config.get("email","fromMail")
        toMail=config.get("email","toMail")
        cc=config.get("email","cc")
        username=config.get("email","username")
        password=config.get("email","password")
#    print smtpHost,smtpPort,sslPort,fromMail,username,password,toMail,cc
    return smtpHost,smtpPort,sslPort,fromMail,toMail,cc,username,password,




class smail(object):
    def send_errormsg(self,str1,body,basepath):
        smtpHost=readmsg()[0]
        smtpPort =readmsg()[1]
        sslPort  = readmsg()[2]
        fromMail = readmsg()[3]
        toMail=readmsg()[4].split(',')
        cc=readmsg()[5].split(',')
#发邮件的用户名和密码
        username = readmsg()[6]
        password = readmsg()[7]
        msg = MIMEMultipart()
        self.str1=str1
        self.body=body
        self.basepath=basepath

#解决中文问题
        reload(sys)
#邮件标题和内容
      #  subject  = u'页面监控情况'
        subject=body+"[andorid "+readconfig.readappinstallmsg()[1]+"]"
#初始化邮件
        encoding = 'utf-8'
        msg['Subject'] = Header(subject,encoding)
        msg['From'] = fromMail
        msg['To'] = ','.join(toMail)
#msg['To'] = toMail
        msg['Date'] = formatdate()
        msg['Cc'] =','.join(cc)

        mail = MIMEText(self.body.encode(encoding),'plain',encoding)
        msg.attach(mail)

        self.basepath="D:/screen/nologin/"
        path1=self.basepath+self.str1

        print path1

        msg.attach(MIMEText('<html><body><h1>%s</h1>'%self.body
                            + '<p><img src="cid:0" width="20%"></p>'
                            +'</body></html>', 'html', 'utf-8'))

        with open(path1, 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
            mime = MIMEBase('image', 'png', filename=self.str1)
    # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename=self.str1)
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
            mime.set_payload(f.read())
    # 用Base64编码:
            encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
            msg.attach(mime)

        att1 = MIMEText(open(path1, 'rb').read(), 'base64', 'gb2312')
        att1.add_header('Content-ID', '<image1>')
        att1["Content-Type"] = 'application/octet-stream'

        att1["Content-Disposition"] = 'attachment; filename=%s'%self.str1#这里的filename可以任意写，写什么名字，邮件中显示什么名字
        msg.attach(att1)
        try:
            smtp = smtplib.SMTP_SSL(smtpHost,sslPort)
            smtp.ehlo()
            smtp.login(username,password)
            toaddress=toMail+cc
            smtp.sendmail(fromMail,toaddress,msg.as_string())

            smtp.close()
            print 'OK'
        except Exception:
            print 'Error: unable to send email'

