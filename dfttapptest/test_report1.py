#coding:utf-8
import os
import calendar
import xlrd,xlwt,xlsxwriter
from xlutils.copy import copy
def get_format_center(wd,size):
    return wd.add_format({'align': 'left','valign': 'vcenter','font_size': size,'border':1})
# 写数据
def _write_center(worksheet, cl, data, wd):
    return worksheet.write(cl, data, get_format_center(wd,9))

def eachFile(filepath):
    dir=[]
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        dir.append(child.decode('gbk'))
    return dir
def testfileexists(filepath):
    if not os.path.exists(filepath):
        w= xlwt.Workbook()
        w.add_sheet(u'Sheet1')
        w.save(filepath)
    else:
        pass

def calend(n):
    m=0
    print calendar.month(2017, n)
    total=calendar.monthcalendar(2016, 8)
    for i in total:
        for j in i[1:6]:
            if j!=0:
                m=m+1
    return m

def readexcel(path,file):
    list=[u"01-需求分解",u"02-测试计划",u"03-用例设计",u"04-测试执行",u"05-缺陷报告及验证",u"06-测试报告",u"07-配置管理",u"08-脚本开发",u"09-升级捆绑",u"10-数据监控",u"11-测试管理",u"12-其他"]
    #将得到的数据写到一张临时表里面
    #------------------
    num01,num02,num03,num04,num05,num06,num07,num08,num09,num10,num11,num12=0,0,0,0,0,0,0,0,0,0,0,0
    if path.name[0:5]!='Sheet':
        sheet=data.sheet_by_name(path.name)
        for j in range(1,sheet.nrows):
            if sheet.cell_value(j,7):
                if 'h' in str(sheet.cell_value(j,7)) or 'H' in str(sheet.cell_value(j,7)):
                    unit=float((sheet.cell_value(j,7))[0:len(sheet.cell_value(j,7))-1])
                else:
                    unit=float(sheet.cell_value(j,7))
                if sheet.cell_value(j,2)==list[0]:
                    num01=num01+unit
                if sheet.cell_value(j,2)==list[1]:
                    num02=num02+unit
                if sheet.cell_value(j,2)==list[2]:
                    num03=num03+unit
                if sheet.cell_value(j,2)==list[3]:
                    num04=num04+unit
                if sheet.cell_value(j,2)==list[4]:
                    num05=num05+unit
                if sheet.cell_value(j,2)==list[5]:
                    num06=num06+unit
                if sheet.cell_value(j,2)==list[6]:
                    num07=num07+unit
                if sheet.cell_value(j,2)==list[7]:
                    num08=num08+unit
                if sheet.cell_value(j,2)==list[8]:
                    num09=num09+unit
                if sheet.cell_value(j,2)==list[9]:
                    num10=num10+unit
                if sheet.cell_value(j,2)==list[10]:
                    num11=num11+unit
                if sheet.cell_value(j,2)==list[11]:
                    num12=num12+unit
        print path.name,[num01,num02,num03,num04,num05,num06,num07,num08,num09,num10,num11,num12]
        list=[path.name,num01,num02,num03,num04,num05,num06,num07,num08,num09,num10,num11,num12]
        sl=xlrd.open_workbook(file)
        xl=copy(sl)
        xs=xl.get_sheet(0)
        nr=sl.sheet_by_name("Sheet1").nrows
        for i in list:
            xs.write(nr,list.index(i),i)
        xl.save(file)

def writereport(file):
    workbook = xlsxwriter.Workbook(file)
    worksheet = workbook.add_worksheet("Sheet1")
    # 设置列行的宽高
    worksheet.set_column("A:A", 9)
    worksheet.set_column("B:B", 9)
    worksheet.set_column("C:C", 9)
    worksheet.set_column("D:D", 9)
    worksheet.set_column("E:E", 9)
    worksheet.set_column("F:F", 9)
    worksheet.set_column("G:G", 9)
    worksheet.set_column("H:H", 9)
    worksheet.set_column("I:I", 9)
    worksheet.set_column("J:J", 9)
    worksheet.set_column("K:K", 9)
    worksheet.set_column("L:L", 9)
    worksheet.set_column("M:M", 9)
    worksheet.set_column("N:N", 9)
    worksheet.set_column("O:O", 9)
    worksheet.set_column("P:P", 9)
    worksheet.set_column("Q:Q", 9)
    worksheet.set_column("R:R", 9)
    worksheet.set_column("S:S", 9)
    worksheet.set_column("T:T", 9)
    for i in range(13):
        worksheet.set_row(i, 12)

filepath="E:\\mac\\report1\\"
file="E:\\mac\\report\\result.xls"
filereport="E:\\mac\\report\\report.xls"
testfileexists(file)
testfileexists(filereport)
alldir=eachFile(filepath)
for i in alldir:
    data=xlrd.open_workbook(i)
    sheetall=data.sheets()
    for j in sheetall:
        readexcel(j,file)

writereport(filereport)