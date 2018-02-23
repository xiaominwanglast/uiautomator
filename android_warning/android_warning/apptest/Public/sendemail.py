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
import xlrd
from apptest.Public.write_summary import readdst
'''
def readmsg():
    config = ConfigParser.ConfigParser()
    try:
        with open(os.path.dirname(os.getcwd())+"\\config\\config.ini","r") as cfgfile:
            config.readfp(cfgfile)
            smtpHost=config.get("email","smtpHost")
            smtpPort=config.get("email","smtpPort")
            sslPort=config.get("email","sslPort")
            fromMail=config.get("email","fromMail")
            toMail=config.get("email","toMail")
            cc=config.get("email","cc")
            username=config.get("email","username")
            password=config.get("email","password")
    except:
        with open(os.path.dirname(os.path.dirname(os.getcwd()))+"\\config\\config.ini","r") as cfgfile:
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

'''

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
        subject=u"[东方头条](报警)"+body+"[android "+readconfig.readappinstallmsg()[1]+"_"+time.strftime('%Y%m%d',time.localtime(time.time()))+"]"
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

        smtpHost=readmsg()[0]
        smtpPort =readmsg()[1]
        sslPort  = readmsg()[2]


        fromMail = readmsg()[3]

        toMail=readmsg()[4].split(',')

        cc=readmsg()[5].split(',')


#发邮件的用户名和密码
        username = readmsg()[6]
        password = readmsg()[7]
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




    def send_msgonly(self,subject,body):
        msg = MIMEMultipart()
        self.body=body
        self.subject=subject

        smtpHost=readmsg()[0]
        smtpPort =readmsg()[1]
        sslPort  = readmsg()[2]


        fromMail = readmsg()[3]

        toMail=readmsg()[4].split(',')

        cc=readmsg()[5].split(',')


#发邮件的用户名和密码
        username = readmsg()[6]
        password = readmsg()[7]


#解决中文问题
        reload(sys)


#邮件标题和内容
#        subject  = u'服务器接口情况'

#初始化邮件
        encoding = 'utf-8'

        msg['Subject'] = Header(self.subject,encoding)
        msg['From'] = fromMail
        msg['To'] = ','.join(toMail)
        msg['Date'] = formatdate()
        msg['Cc'] =','.join(cc)


#        mail = MIMEText(self.body.encode(encoding),'plain',encoding)
        msg.attach(MIMEText('<html><body><h1>%s</h1>'%self.body
                            + '<p><img src="cid:0" width="20%"></p>'
                            +'</body></html>', 'html', 'utf-8'))
#        msg.attach(mail)


        try:

            smtp = smtplib.SMTP_SSL(smtpHost,sslPort)
            smtp.ehlo()
            smtp.login(username,password)
            print "111"
    #发送邮件
            toaddress=toMail+cc
            smtp.sendmail(fromMail,toaddress,msg.as_string())

            smtp.close()
            print 'OK'

        except Exception as e:
            print e
            print 'Error: unable to send email'
#smail().send_msgonly(u"运行情况",u"手机网络异常")


    def setuireport(self,filepath,filepath1):
        msg = MIMEMultipart()
        data=readdst(filepath1)[5]
        if str(data)=="100.00%":
            self.subject=u"【东方头条】空白页预警测试报告-通过"+"[android "+readconfig.readappinstallmsg()[1]+"_"+time.strftime('%Y%m%d',time.localtime(time.time()))+"]"
        else:
            self.subject=u"【东方头条】空白页预警测试报告-通过率"+ str(data) +"[android "+readconfig.readappinstallmsg()[1]+"_"+time.strftime('%Y%m%d',time.localtime(time.time()))+"]"
        smtpHost=readmsg()[0]
        smtpPort =readmsg()[1]
        sslPort  = readmsg()[2]


        fromMail = readmsg()[3]

        toMail=readmsg()[4].split(',')

        cc=readmsg()[5].split(',')


#发邮件的用户名和密码
        username = readmsg()[6]
        password = readmsg()[7]


#解决中文问题
        reload(sys)

#初始化邮件
        encoding = 'utf-8'

        msg['Subject'] = Header(self.subject,encoding)
        msg['From'] = fromMail
        msg['To'] = ','.join(toMail)
        msg['Date'] = formatdate()
        msg['Cc'] =','.join(cc)
        header='<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head>'
#        th='<body><table border="1" cellspacing="0" cellpadding="3" width="800" align="left" ><align="center" ><th>标识</th></tr>'
        th='<body><table border="1" cellspacing="0" cellpadding="3" width="800" align="left" ><tr align="center" ><td colspan="6"> 【东方头条】Android端UI测试报告</td></tr>'

#打开文件

        book=xlrd.open_workbook(filepath)
        sheet=book.sheet_by_index(0)
#获取行列的数目，并以此为范围遍历获取单元数据
        nrows = sheet.nrows-1
        ncols = sheet.ncols
        body=''
        # cellData=1

        # print nrows,ncols

        # tip='<td>'+u'app名称'+'</td>'+'<td>'+'2222'+'</td>'+'<td>'+u'平台'+'</td>'+'<td>'+'4444'+'</td>'+'<td>'+u'回归用例数'+'</td>'+'<td>'+'6666'+'</td>'


        for i in range(1,nrows+1):
            td=''
            for j in range(ncols):
                cellData=sheet.cell_value(i,j)
       #         print type(cellData),cellData

                if isinstance(cellData,float):
                    if cellData>=0:
                        cellData=int(cellData)
                        cellData=str(cellData)
                    elif i==nrows and j==ncols-1:
                        cellData=str(cellData*100)+"%"
                    # print "--------------"
                    # print type(cellData)

                tip='<td>'+cellData+'</td>'
                td=td+tip

            tr='<tr>'+td+'</tr>'
            tr=tr.encode('utf-8')
            body=body+tr

        # print body
#        tr='<tr>'+td+'</tr>'+'<tr>'+td+'</tr>'
        tail='</table></body></html>'
#打开文件
        mail=header+th+body+tail
#        mail = MIMEText(self.body.encode(encoding),'plain',encoding)
        msg.attach(MIMEText(mail ,'html', 'utf-8'))
#        msg.attach(mail)

        att3 = MIMEText(open(filepath1, 'rb').read(), 'base64', 'gb2312')
        att3["Content-Type"] = 'application/octet-stream'
        att3["Content-Disposition"] = 'attachment; filename="ResultReport_warning.xls"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
        msg.attach(att3)

        try:
            smtp = smtplib.SMTP_SSL(smtpHost,sslPort)
            smtp.ehlo()
            smtp.login(username,password)

    #发送邮件
            toaddress=toMail+cc
            smtp.sendmail(fromMail,toaddress,msg.as_string())

            smtp.close()
            print 'OK'

        except Exception as e:
            print e
            print 'Error: unable to send email'


#smail().send_msgonly(u"运行情况",u"手机网络异常")
#smail().setuireport("E:\\wxm\\pycharm\\python\\android_warning\\apptest\\result\\excel\\2016-12-21\\report.xls")