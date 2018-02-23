# -*- coding: UTF-8 -*-
import smtplib
from email.utils import formatdate
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from apptest.Public.write_summary import readdst
from apptest.Public import readconfig
from email.mime.multipart import MIMEMultipart
import sys
import time
import ConfigParser,os
import xlrd

class smail:
    def sendreport(self,filepath,filepath1,filepath2):
        msg = MIMEMultipart()
        data=readdst(filepath1)[5]
        if str(data)=="100.00%":
            self.subject=u"【东方头条】空白页预警测试报告-通过"+"[android "+readconfig.readappinstallmsg()[1]+"_"+time.strftime('%Y%m%d',time.localtime(time.time()))+"]"
        else:
            self.subject=u"【东方头条】空白页预警测试报告-通过率"+ str(data) +"[android "+readconfig.readappinstallmsg()[1]+"_"+time.strftime('%Y%m%d',time.localtime(time.time()))+"]"
        smtpHost=readmsg()[0]
        sslPort  = readmsg()[2]
        fromMail = readmsg()[3]
        toMail=readmsg()[4].split(',')
        cc=readmsg()[5].split(',')
#发邮件的用户名和密码
        username = readmsg()[6]
        password = readmsg()[7]

        reload(sys)
#初始化邮件
        encoding = 'utf-8'
        msg['Subject'] = Header(self.subject,encoding)
        msg['From'] = fromMail
        msg['To'] = ','.join(toMail)
        msg['Date'] = formatdate()
        msg['Cc'] =','.join(cc)

        #添加html内容
        header='<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head>'
        th='<body><table border="1" cellspacing="0" cellpadding="3" width="800" align="left" ><tr align="center" ><td colspan="6"> 【东方头条】Android端UI测试报告</td></tr>'
        #打开文件
        book=xlrd.open_workbook(filepath)
        sheet=book.sheet_by_index(0)
        #获取行列的数目，并以此为范围遍历获取单元数据
        nrows = sheet.nrows-1
        ncols = sheet.ncols
        body=''
        for i in range(1,nrows+1):
            td=''
            for j in range(ncols):
                cellData=sheet.cell_value(i,j)
                if isinstance(cellData,float):
                    if cellData>=0:
                        cellData=int(cellData)
                        cellData=str(cellData)
                    elif i==nrows and j==ncols-1:
                        cellData=str(cellData*100)+"%"
                tip='<td>'+cellData+'</td>'
                td=td+tip
            tr='<tr>'+td+'</tr>'
            tr=tr.encode('utf-8')
            body=body+tr
        body=body+'</table>'
        tail='</table></body></html>'
        if os.path.exists(filepath2):
            tip1='<table border="0" cellspacing="0" cellpadding="3" width="800" height="50" align="left" ><tr align="left"><td colspan="6"><font size="3">如下为空白页预警测试Fail详细情况</td></tr></table>'
            title='<table border="1" cellspacing="0" cellpadding="3" width="1000" align="left" ><tr align="center" ><td><b>用例名称</b></td><td><b>操作步骤</b></td><td><b>预期结果</b></td><td><b>测试结果</b></td><td><b>备注</b></td></tr>'
            work_body = xlrd.open_workbook(filepath2)
            dst = xlrd.open_workbook(filepath1)
            dst_sheet=dst.sheet_by_name('Android')
            body_sheet = work_body.sheet_by_name('Sheet1')
            body2=''
            for i in range(body_sheet.nrows):
                td2=''
                if body_sheet.cell_value(i,0).strip()=='login.test_02_trykillappium':
                    td2='<td>登陆</td><td>1）手机账号登录 2）微信账号登录3）QQ账号登录 4）微博账号登录，四种方式随机登陆</td><td>登陆成功</td><td>Fail</td><td>我的>手机登录-登录异常</td>'
                for j in range(1,dst_sheet.nrows):
                    if body_sheet.cell_value(i,0).strip()==dst_sheet.cell_value(j,12).strip():
                        td2='<td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>'%(dst_sheet.cell_value(j,2),dst_sheet.cell_value(j,4),dst_sheet.cell_value(j,5),dst_sheet.cell_value(j,10),body_sheet.cell_value(i,3))
                td2='<tr>'+td2+'</tr>'
                body2=body2+td2.encode('utf-8')
            tip2='<table border="0" cellspacing="0" cellpadding="3" width="1000" height="50" align="left" ><tr align="left"><td colspan="6"><font color="#0000FF" size="3">备注：</td></tr>'
            tip3='<tr align="left"><td colspan="6"><font color="#0000FF" size="3">1>Fail的用例失请人工测试，复测；</td></tr>'
            tip4='<tr align="left"><td colspan="6"><font color="#0000FF" size="3">2>报告详情见附件(测试fail截图同放附件)；</td></tr>'
            mail=header+th+body+tip1+title+body2+'</table>'+tip2+tip3+tip4+tail
        else:
            mail=header+th+body+tail
        msg.attach(MIMEText(mail ,'html', 'utf-8'))

        '''
        if os.path.exists(filepath2):
            workbook = xlrd.open_workbook(filepath2)
            sheet1 = workbook.sheet_by_name('Sheet1')
            xlsrows=sheet1.nrows
            for i in range(1,xlsrows+1):
                body=sheet1.cell(i-1,3).value
                path1=sheet1.cell(i-1,2).value
                str1=os.path.basename(path1)
                mail = MIMEText(body.encode(encoding),'plain',encoding)
                msg.attach(mail)
    #        basepath="D:/screen/nologin/"
                msg.attach(MIMEText('<html><body><ul type="disc" align="up"><li> <font size="5" color="blue"><strong>%s</strong></font>'%body+'</li>'
                             +'<li><img src="cid:'+str(i)+'" width="20%"></li>'
                             +'</ul></body></html>', 'html', 'utf-8'))
                with open(path1, 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
                    mime = MIMEBase('image', 'png', filename=str1)
    # 加上必要的头信息:
                    mime.add_header('Content-Disposition', 'attachment', filename=str1)
                    mime.add_header('Content-ID', '<%i>'%i)
                    mime.add_header('X-Attachment-Id', '%i'%i)
    # 把附件的内容读进来:
                    mime.set_payload(f.read())
    # 用Base64编码:
                    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
                    msg.attach(mime)
            '''

        #添加总的测试报告
        att2= MIMEText(open(filepath1, 'rb').read(), 'base64', 'gb2312')
        att2["Content-Type"] = 'application/octet-stream'
        att2["Content-Disposition"] = 'attachment; filename="ResultReport_warning.xls"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
        msg.attach(att2)

        #添加fail测试报告
        if os.path.exists(filepath2):
            #逐行读取报告放入附件
            workbook = xlrd.open_workbook(filepath2)
            sheet1 = workbook.sheet_by_name('Sheet1')
            xlsrows=sheet1.nrows
            for i in range(0,xlsrows):
                path1=sheet1.cell(i,2).value
                str1=os.path.basename(path1)
                att = MIMEText(open(path1, 'rb').read(), 'base64', 'utf-8')
                att["Content-Type"] = 'application/octet-stream'
                att["Content-Disposition"] = 'attachment; filename="%s"'%str1
                msg.attach(att)

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
def readmsg():
    config = ConfigParser.ConfigParser()
    filejudge=os.path.dirname(os.getcwd())
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
    return smtpHost,smtpPort,sslPort,fromMail,toMail,cc,username,password,

if __name__=='__main__':
    dstdirname=os.path.dirname(os.getcwd())+'\\result\\excel'
    report=dstdirname+"\\"+"report.xls"
    dstfile=dstdirname+"\\"+"ResultReport_warning.xls"
    failpath=dstdirname+"\\"+"FailureReport.xls"
    smail().sendreport(report,dstfile,failpath)
