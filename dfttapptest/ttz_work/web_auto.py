#coding:utf-8
import requests
import re,time
import xlrd,xlwt
import os
import csv,sys
import smtplib
from email.utils import formatdate
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def get_testurl():
    url_list=[]
    url_book=xlrd.open_workbook(url_path)
    url_sheet=url_book.sheet_by_name('Sheet1')
    for i in range(url_sheet.nrows):
        try:
            dic={}
            if url_sheet.cell_value(i,1)!='':
                dic['name']=url_sheet.cell_value(i,0).strip()
                dic['url']=url_sheet.cell_value(i,1).strip()
                dic['qid_url']=url_sheet.cell_value(i,2).strip()
                url_list.append(dic)
        except:
            print u'确保url表，第二与第三列数据正常，并且对应关系正确'
            time.sleep(2)
            sys.exit(0)
    return url_list
def geturl():
    start_time=time.time()
    test_url=get_testurl()
    for l in test_url:
        dic_name=l['name']
        wookbook=xlrd.open_workbook(data_path)
        sheet=wookbook.sheet_by_name(dic_name)
        row=sheet.nrows
        csvfile = file(temp_path+dic_name+'.csv', 'wb')
        writer = csv.writer(csvfile)
        for i in range(1,row):
            if sheet.cell_value(i,1) !='':
                qid=sheet.cell_value(i,1)
                if type(qid)==float:
                    qid=str(int(qid))
                else:
                    qid=qid.replace('=','_')
                url=l['qid_url'].replace('null',qid).replace('NUM',str(int(time.time()*1000)))
                resource(qid,url,writer)
                sys.stdout.write(u'当前{}总进度为{}%\r'.format(dic_name,i*100/(row-1)))
                sys.stdout.flush()
        csvfile.close()
    end_time=time.time()
    print u'发费总时间为{}秒'.format(int(end_time-start_time))
def resource(qid,url,writer,t=0):
    id_list=[]
    try:
        html=requests.get(url,timeout=4)
    except:
        t+=1
        if t<4:
            resource(qid,url,writer,t=t)
    else:
        if html.status_code==404:
            pass
        else:
            id_list=re.findall('id:\'(.*?)\'',html.text)
        id_list=[i for i in id_list if i!='default']
        id_list.insert(0,qid)
        writer.writerow(id_list)

def write_result():
    test_url=get_testurl()
    wbk=xlwt.Workbook()
    for i in test_url:
        csv_r=csv.reader(file(temp_path+i['name']+'.csv'))
        sheet=wbk.add_sheet(i['name'],cell_overwrite_ok=True)
        line=1
        for j in csv_r:
            if i['name']==u'图片站' and len(j)==10:
                j[7]=''
                j[8]=''
            if i['name']==u'频道页' and len(j)==8:
                j[7]=''
            if i['name']==u'详情页' and len(j)==25:
                j[20]=''
            if i['name']==u'分页页面' and len(j)==7:
                j[4]=''
                j[5]=''
            for k in range(len(j)):
                sheet.write(line,k,j[k])
            line+=1
        wbk.save(test_result)
def testfileexists():
    name_list=[u'首页.csv',u'分页页面.csv',u'图片站.csv',u'详情页.csv',u'频道页.csv']
    for i in name_list:
        work_temp=temp_path+ i
        if os.path.exists(work_temp):
            os.remove(work_temp)
    if os.path.exists(test_result):
        os.remove(test_result)
    if os.path.exists(diff_path):
        os.remove(diff_path)
def get_result():
    wbk=xlwt.Workbook()
    resource_book=xlrd.open_workbook(data_path)
    temp_book=xlrd.open_workbook(test_result)
    for i in temp_book.sheets():
        sheet=wbk.add_sheet(i.name,cell_overwrite_ok=True)
        temp_sheet=temp_book.sheet_by_name(i.name)
        resource_sheet=resource_book.sheet_by_name(i.name)
        if i.name==u"分页页面":
            temp_sheet.ncols=4
        for j in range(temp_sheet.nrows):
            for k in range(1,temp_sheet.ncols):
                temp_cell=temp_sheet.cell_value(j,k)
                resource_cell=resource_sheet.cell_value(j,k+1)
                try:
                    temp_cell=float(temp_cell)
                    if temp_cell!=resource_cell:
                        sheet.write(j,0,temp_sheet.cell_value(j,0))
                        if resource_cell=='':
                            resource_cell=u'异常'
                        sheet.write(j,k,resource_cell)
                except:
                    if temp_cell!=resource_cell:
                        sheet.write(j,0,temp_sheet.cell_value(j,0))
                        if resource_cell=='':
                            resource_cell=u'异常'
                        sheet.write(j,k,resource_cell)
        wbk.save(diff_path)
def readeconfig(emailpath):
    emaillist=[]
    src=xlrd.open_workbook(emailpath)
    rows=src.sheet_by_name('Sheet1').nrows
    for i in range(rows):
        emaillist.append(src.sheet_by_name('Sheet1').cell_value(i,2))
    return emaillist
def setuireport(emailpath):
    config=readeconfig(emailpath)
    msg = MIMEMultipart()
    subject=u'H5_web测试报告_%s'%time.strftime('%Y%m%d',time.localtime(time.time()))
    smtpHost='smtp.exmail.qq.com'
    smtpPort =25
    sslPort  = 465

    fromMail = config[0]
    toMail=config[1].split(',')
    cc=config[2].split(',')

#发邮件的用户名和密码
    username = config[3]
    password = config[4]
#解决中文问题
    reload(sys)
#初始化邮件
    encoding = 'utf-8'
    msg['Subject'] = Header(subject,encoding)
    msg['From'] = fromMail
    msg['To'] = ','.join(toMail)
    msg['Date'] = formatdate()
    msg['Cc'] =','.join(cc)
#附加附件

    att3 = MIMEText(open(data_path, 'rb').read(), 'base64', 'gb2312')
    att3["Content-Type"] = 'application/octet-stream'
    att3["Content-Disposition"] = 'attachment; filename="%s"'%(u'h5页面位置表.xlsx'.encode('gb2312'))#这里的filename可以任意写，写什么名字，邮件中显示什么名字
    msg.attach(att3)

    att2 = MIMEText(open(test_result, 'rb').read(), 'base64', 'gb2312')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="h5_temp.xlsx"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
    msg.attach(att2)

    att4 = MIMEText(open(diff_path, 'rb').read(), 'base64', 'gb2312')
    att4["Content-Type"] = 'application/octet-stream'
    att4["Content-Disposition"] = 'attachment; filename="result.xlsx"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
    msg.attach(att4)
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
        print 'Error: unable to send email,please check'

if __name__=='__main__':
    url_path=os.path.dirname(os.getcwd())+'\\ttz_work\\'+'url.xls'
    data_path=os.path.dirname(os.getcwd())+'\\ttz_work\\'+u'头条后台ID表.xls'
    temp_path=os.path.dirname(os.getcwd())+'\\ttz_work\\'
    email_path=os.path.dirname(os.getcwd())+'\\ttz_work\\'+'send_email.xls'
    test_result=os.path.dirname(os.getcwd())+'\\ttz_work\\'+'web_temp.xlsx'
    diff_path=os.path.dirname(os.getcwd())+'\\ttz_work\\'+'result.xlsx'

    print u"WEB_头条站自动化打包版本V20170420.1".encode('gb18030')
    print u"目前采用协议与JS数据包进行自动测试，无界面(非selenium自动化)".encode('gb18030')
    print "-----------------------------------------------------------"
    time.sleep(1)
    print u"开始测试······".encode('gb18030')
    testfileexists()
    geturl()
    write_result()
    get_result()
    if os.path.exists(test_result) and os.path.exists(diff_path):
        print u"发送邮件······".encode('gb18030')
        setuireport(email_path)
    print u"测试完成······".encode('gb18030')
    time.sleep(2)
