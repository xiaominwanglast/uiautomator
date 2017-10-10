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
            if i !='':
                qid=sheet.cell_value(i,0)
                if type(qid)==float:
                    qid=str(int(qid))
                url=l['qid_url'].replace('null',qid)
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
            for k in range(len(j)):
                sheet.write(line,k,j[k])
            line+=1
        wbk.save(test_result)
def get_result():
    wbk=xlwt.Workbook()
    resource_book=xlrd.open_workbook(data_path)
    temp_book=xlrd.open_workbook(test_result)
    for i in temp_book.sheets():
        sheet=wbk.add_sheet(i.name,cell_overwrite_ok=True)
        temp_sheet=temp_book.sheet_by_name(i.name)
        resource_sheet=resource_book.sheet_by_name(i.name)
        for j in range(temp_sheet.nrows):
            for k in range(1,temp_sheet.ncols):
                temp_cell=temp_sheet.cell_value(j,k)
                resource_cell=resource_sheet.cell_value(j,k)
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
def testfileexists():
    name_list=[u'头条列表页.csv',u'头条内页.csv',u'头条图片内页.csv']
    for i in name_list:
        work_temp=temp_path+ i
        if os.path.exists(work_temp):
            os.remove(work_temp)
    if os.path.exists(test_result):
        os.remove(test_result)
    if os.path.exists(diff_path):
        os.remove(diff_path)
if __name__=='__main__':
    url_path=os.path.dirname(os.getcwd())+'\\h5_work\\'+'url.xlsx'
    data_path=os.path.dirname(os.getcwd())+'\\h5_work\\'+u'h5页面位置表.xlsx'
    email_path=os.path.dirname(os.getcwd())+'\\h5_work\\'+'send_email.xls'
    temp_path=os.path.dirname(os.getcwd())+'\\h5_work\\'
    test_result=os.path.dirname(os.getcwd())+'\\h5_work\\'+'h5_temp.xlsx'
    diff_path=os.path.dirname(os.getcwd())+'\\h5_work\\'+'result.xlsx'

    print u"H5_web自动化打包版本V20170419.1".encode('gb18030')
    print u"目前采用协议与JS数据包进行自动测试，无界面(非selenium自动化)".encode('gb18030')
    print "-----------------------------------------------------------"
    print u"***确保url表测试url与广告JS加载的数据链路url正确以及对应正确(新增url类型由自动化组维护)".encode('gb18030')
    print u"***后期测试哪一类型url，就写上url与第三列对用的广告JS数据链路url，不测的话两个url都不要写".encode('gb18030')
    print u"***确保执行文件名为h5_work不要改动".encode('gb18030')
    print u"***确保email表邮件配置正确，cc抄送不能为空并且分隔符逗号为英文形式".encode('gb18030')
    print u"***测试生成h5_temp总表，单个url对应的表，与差异表result(差异表是对比h5_temp与h5页面位置表差异，写入的qid与h5页面位置表数据)".encode('gb18030')
    print u"***注意若result差异表中有'异常'标志,表示h5页面位置表数据对应数据显示为空，而实际h5_temp已抓出广告id数据".encode('gb18030')
    print u"***程序出现异常或者h5_temp数据异常时直接联系自动化组进行更新维护".encode('gb18030')
    print "-----------------------------------------------------------"

    time.sleep(2)
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
