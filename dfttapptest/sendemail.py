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



class smail(object):
    def send_errormsg(self,str1,body,basepath):

        msg = MIMEMultipart()
        self.str1=str1
        self.body=body
        self.basepath=basepath

#发送邮件的相关信息，根据实际情况填写
        smtpHost = 'smtp.exmail.qq.com'
        smtpPort = '25'
        sslPort  = '465'
        fromMail = 'wangxiaomin@021.com'
#添加发件人
        toMail =['wangxiaomin@021.com','2274052689@qq.com']
#添加抄送人
        cc = ['wangxiaomin@163.com']
#发邮件的用户名和密码
        username = 'wangxiaomin@021.com'
        password = '992623Wang'
#解决中文问题
        reload(sys)


#邮件标题和内容
        subject  = u'页面监控情况'
        body     = u'测试结果'


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

#        basepath="D:/screen/nologin/"
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


#        att2 = MIMEText(open('G:\\testreport\\interface\\testurl.xls', 'rb').read(), 'base64', 'gb2312')
#        att2["Content-Type"] = 'application/octet-stream'
#        att2["Content-Disposition"] = 'attachment; filename="testurl.xls"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
#        msg.attach(att2)

        #这里需要添加htmltestreport

#        att3 = MIMEText(open('G:\\testreport\\htmlreport\\test_report.zip', 'rb').read(), 'base64', 'gb2312')
#        att3["Content-Type"] = 'application/octet-stream'
#        att3["Content-Disposition"] = 'attachment; filename="test_report.zip"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
#        msg.attach(att3)

#可以继续添加附件

#att2 = MIMEText(open('d:\\123.rar', 'rb').read(), 'base64', 'gb2312')
#att2["Content-Type"] = 'application/octet-stream'
#att2["Content-Disposition"] = 'attachment; filename="123.rar"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
#msg.attach(att2)


        try:
    #连接smtp服务器，明文/SSL/TLS三种方式，根据你使用的SMTP支持情况选择一种
    #普通方式，通信过程不加密
    #smtp = smtplib.SMTP(smtpHost,smtpPort)
    #smtp.ehlo()
    #smtp.login(username,password)

    #tls加密方式，通信过程加密，邮件数据安全，使用正常的smtp端口
    #smtp = smtplib.SMTP(smtpHost,smtpPort)
    #smtp.ehlo()
    #smtp.starttls()
    #smtp.ehlo()
    #smtp.login(username,password)

    #纯粹的ssl加密方式，通信过程加密，邮件数据安全
            smtp = smtplib.SMTP_SSL(smtpHost,sslPort)
            smtp.ehlo()
            smtp.login(username,password)

    #发送邮件
            toaddress=toMail+cc
            smtp.sendmail(fromMail,toaddress,msg.as_string())

            smtp.close()
            print 'OK'
        except Exception:
            print 'Error: unable to send email'

#stime=time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

#print str(stime+".png")
#smail().send("2016-08-31-10_35_0.png")

    def send_report(self):
        msg = MIMEMultipart()

#发送邮件的相关信息，根据实际情况填写
        smtpHost = 'smtp.exmail.qq.com'
        smtpPort = '25'
        sslPort  = '465'
        fromMail = 'yueguanwen@021.com'
#添加发件人
        toMail =['yueguanwen@021.com','2880263944@qq.com']
#添加抄送人
        cc = ['yueguanwen@163.com']
#发邮件的用户名和密码
        username = 'yueguanwen@021.com'
        password = 'gaoxin128A'
#解决中文问题
        reload(sys)

#邮件标题和内容
        subject  = u'自动化测试报告'
        body     = u'测试报告情况见附件'


#初始化邮件
        encoding = 'utf-8'


        msg['Subject'] = Header(subject,encoding)
        msg['From'] = fromMail
        msg['To'] = ','.join(toMail)
#msg['To'] = toMail
        msg['Date'] = formatdate()
        msg['Cc'] =','.join(cc)

        mail = MIMEText(body.encode(encoding),'plain',encoding)
        msg.attach(mail)


        #这里需要添加htmltestreport

        att3 = MIMEText(open('G:\\testreport\\htmlreport\\test_report.zip', 'rb').read(), 'base64', 'gb2312')
        att3["Content-Type"] = 'application/octet-stream'
        att3["Content-Disposition"] = 'attachment; filename="test_report.zip"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
        msg.attach(att3)

#可以继续添加附件

#att2 = MIMEText(open('d:\\123.rar', 'rb').read(), 'base64', 'gb2312')
#att2["Content-Type"] = 'application/octet-stream'
#att2["Content-Disposition"] = 'attachment; filename="123.rar"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
#msg.attach(att2)


        try:
    #连接smtp服务器，明文/SSL/TLS三种方式，根据你使用的SMTP支持情况选择一种
    #普通方式，通信过程不加密
    #smtp = smtplib.SMTP(smtpHost,smtpPort)
    #smtp.ehlo()
    #smtp.login(username,password)

    #tls加密方式，通信过程加密，邮件数据安全，使用正常的smtp端口
    #smtp = smtplib.SMTP(smtpHost,smtpPort)
    #smtp.ehlo()
    #smtp.starttls()
    #smtp.ehlo()
    #smtp.login(username,password)

    #纯粹的ssl加密方式，通信过程加密，邮件数据安全
            smtp = smtplib.SMTP_SSL(smtpHost,sslPort)
            smtp.ehlo()
            smtp.login(username,password)

    #发送邮件
            toaddress=toMail+cc
            smtp.sendmail(fromMail,toaddress,msg.as_string())

            smtp.close()
            print 'OK'
        except Exception:
            print 'Error: unable to send email'


    def send_service_status(self,body):
        msg = MIMEMultipart()
        self.body=body

#发送邮件的相关信息，根据实际情况填写
        smtpHost = 'smtp.exmail.qq.com'
        smtpPort = '25'
        sslPort  = '465'
        fromMail = 'yueguanwen@021.com'
#添加发件人
        toMail =['yueguanwen@021.com','2880263944@qq.com']
#添加抄送人
        cc = ['yueguanwen@163.com']
#发邮件的用户名和密码
        username = 'yueguanwen@021.com'
        password = 'gaoxin128A'
#解决中文问题
        reload(sys)


#邮件标题和内容
        subject  = u'服务器接口情况'

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


        try:
            smtp = smtplib.SMTP_SSL(smtpHost,sslPort)
            smtp.ehlo()
            smtp.login(username,password)

    #发送邮件
            toaddress=toMail+cc
            smtp.sendmail(fromMail,toaddress,msg.as_string())

            smtp.close()
            print 'OK'
        except Exception:
            print 'Error: unable to send email'


