#coding:utf-8
import os
from time import sleep
import calendar
import xlrd,xlwt,xlsxwriter
from xlutils.copy import copy
def get_format_center(wd,size):
    return wd.add_format({'align': 'left','valign': 'vcenter','font_size': size,'border':1})
# 写数据
def _write_center(worksheet, cl, data, wd):
    return worksheet.write(cl, data, get_format_center(wd,11))

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
        os.remove(filepath)
        w= xlwt.Workbook()
        w.add_sheet(u'Sheet1')
        w.save(filepath)

def calend(n):
    m=0
    total=calendar.monthcalendar(2017, n)
    for i in total:
        for j in i[0:5]:
            if j!=0:
                m=m+1
    return m

def datachoose(data,name,j):
    if '..' in data:
        print (u"!!!%s表第%s行数据%s存在问题，自动去掉重复点,可检查表数据"%(name,j,data))
        data=data.replace('..','.')
    if 'h' in data or 'H' in data:
        unit=float(data[0:len(data)-1])
    else:
        unit=float(data)
    return unit

def readexcel(path,file):
    list=[u"01-需求分解",u"02-测试计划",u"03-用例设计",u"04-脚本开发",u"05-测试执行",u"06-缺陷报告",u"07-缺陷验证",u"08-测试报告",u"09-配置管理",u"10-质量度量",u"11-数据分析",u"12-测试管理",u"13-其他",u"14-休假"]
    #将得到的数据写到一张临时表里面
    #------------------
    num01,num02,num03,num04,num05,num06,num07,num08,num09,num10,num11,num12,num13,num14=0,0,0,0,0,0,0,0,0,0,0,0,0,0
    if path.name[0:5]!='Sheet':
        sheet=data.sheet_by_name(path.name)
        for j in range(1,sheet.nrows):
            if sheet.cell_value(j,7):
                try:
                    unit=datachoose(str(sheet.cell_value(j,7)),sheet.name,j)
                except:
                    print (u"!!!%s表第%s行数据存在问题（数据是汉字），自动赋值为0h,可检查表数据"%(sheet.name,j))
                    unit=0
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
                if sheet.cell_value(j,2)==list[12]:
                    num13=num13+unit
                if sheet.cell_value(j,2)==list[13]:
                    num14=num14+unit
      #  print path.name,[num01,num02,num03,num04,num05,num06,num07,num08,num09,num10,num11,num12,num13]
        list=[path.name,num01,num02,num03,num04,num05,num06,num07,num08,num09,num10,num11,num12,num13,num14]
        sl=xlrd.open_workbook(file)
        xl=copy(sl)
        xs=xl.get_sheet(0)
        nr=sl.sheet_by_name("Sheet1").nrows
        for i in list:
            xs.write(nr,list.index(i),i)
        xl.save(file)

def bug(file,filereport,n):
    list=[u"仲锦",u"张洒洒",u"李鑫",u"徐培杰",u"侯新妮",u"刘伟",u"田振华",u"邓琳仪",u"谭宝林",u"高慧敏",u"程远",u"谭佳佳",u"范石磊",u"何刚"]
    num01,num02,num03,num04,num05,num06,num07,num08,num09,num10,num11,num12,num13,num14=0,0,0,0,0,0,0,0,0,0,0,0,0,0
    num,name=0,0
    number=[]
    if len(n)==1:
        n='0'+n
    alldir=eachFile(filereport)
    for i in alldir:
        if u"产品" in i:
            print i
            dst=xlrd.open_workbook(i)
            dstrows=dst.sheet_by_index(0).nrows
            dstcols=dst.sheet_by_index(0).ncols
            sheet=dst.sheet_by_index(0)
            for i in range(dstcols):
                if dst.sheet_by_index(0).cell_value(0,i)==u"Created":
                    num=i
            for i in range(dstcols):
                if dst.sheet_by_index(0).cell_value(0,i)==u"Creator":
                    name=i
            for i in range(1,dstrows):
                date=xlrd.xldate.xldate_as_datetime(dst.sheet_by_index(0).cell(i,num).value, 0)
                if str(date).split(' ')[0].split('-')[0]=='2017' and str(date).split(' ')[0].split('-')[1]==n:
                    if sheet.cell_value(i,name)==list[0]:
                        num01=num01+1
                    if sheet.cell_value(i,name)==list[1]:
                        num02=num02+1
                    if sheet.cell_value(i,name)==list[2]:
                        num03=num03+1
                    if sheet.cell_value(i,name)==list[3]:
                        num04=num04+1
                    if sheet.cell_value(i,name)==list[4]:
                        num05=num05+1
                    if sheet.cell_value(i,name)==list[5]:
                        num06=num06+1
                    if sheet.cell_value(i,name)==list[6]:
                        num07=num07+1
                    if sheet.cell_value(i,name)==list[7]:
                        num08=num08+1
                    if sheet.cell_value(i,name)==list[8]:
                        num09=num09+1
                    if sheet.cell_value(i,name)==list[9]:
                        num10=num10+1
                    if sheet.cell_value(i,name)==list[10]:
                        num11=num11+1
                    if sheet.cell_value(i,name)==list[11]:
                        num12=num12+1
                    if sheet.cell_value(i,name)==list[12]:
                        num13=num13+1
                    if sheet.cell_value(i,name)==list[13]:
                        num14=num14+1
    listnum=[num01,num02,num03,num04,num05,num06,num07,num08,num09,num10,num11,num12,num13,num14]

    dstresult= xlrd.open_workbook(file)
    dstrows=dstresult.sheet_by_index(0).nrows
    wbre=copy(dstresult)
    for i in range(len(list)):
        for j in range(dstrows):
            if dstresult.sheet_by_index(0).cell_value(j,0)==list[i]:
                wbre.get_sheet(0).write(j,15,listnum[i])
    wbre.save(file)
    return list

def writealldata(file):
    dst= xlrd.open_workbook(file)
    wb=copy(dst)
    dstrows=dst.sheet_by_name("Sheet1").nrows
    dstcols=dst.sheet_by_name("Sheet1").ncols
    for i in range(dstrows):
        for j in range(dstcols):
            if not dst.sheet_by_name("Sheet1").cell_value(i,j):
                wb.get_sheet(0).write(i,j,0)
    wb.save(file)
    try:
        dst.sheet_by_name("Sheet1").cell_value(0,14)
    except:
        for i in range(dstrows):
            wb.get_sheet(0).write(i,14,0)
    wb.save(file)
    newdst= xlrd.open_workbook(file)
    newwb=copy(newdst)
    newrows=newdst.sheet_by_name("Sheet1").nrows
    newcols=newdst.sheet_by_name("Sheet1").ncols
    for i in range(newrows):
        sun=0.0
        for j in range(1,newcols-1):
            sun=sun+float(newdst.sheet_by_name("Sheet1").cell_value(i,j))
        newwb.get_sheet(0).write(i,16,sun)
    newwb.save(file)

def writereport(filepath,file,filereport,m,day):
    list=[u"01-需求分解",u"02-测试计划",u"03-用例设计",u"04-脚本开发",u"05-测试执行",u"06-缺陷报告",u"07-缺陷验证",u"08-测试报告",u"09-配置管理",u"10-质量度量",u"11-数据分析",u"12-测试管理",u"13-其他",u"14-休假"]
    listname=[u"仲锦",u"张洒洒",u"李鑫",u"徐培杰",u"侯新妮",u"刘伟",u"田振华",u"周志勇",u"邓琳仪",u"谭宝林",u"高慧敏",u"程远",u"谭佳佳",u"范石磊",u"何刚",u"岳观文",u"王孝敏",u"许红"]
    listchar=['C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']
    listbugchar=['B','C','D','E','F','G','H','I','J','K','L','M','N','O']
    workbook = xlsxwriter.Workbook(filereport)
    worksheet = workbook.add_worksheet("Sheet1")
    # 设置列行的宽高
    worksheet.set_column("A:A", 20)
    worksheet.set_column("B:B", 11)
    for i in listchar:
        worksheet.set_column("%s:%s"%(i,i), 8)

    for i in range(13):
        worksheet.set_row(i, 12)
    define_format_H1 = workbook.add_format({'bold': 0, 'font_size': 11,'align':'center','border':1})
    define_format_H2 = workbook.add_format({'bold': 1, 'font_size': 11,'align':'center','border':1})
    define_format_H3 = workbook.add_format({'bold': 1, 'font_size': 11,'align':'left','border':1})
    worksheet.merge_range('A2:B2', u"2007年度(上半年)", define_format_H1)

    #第二列
    _write_center(worksheet, "B3", u"工作类型", workbook)
    _write_center(worksheet, "B4", list[0], workbook)
    _write_center(worksheet, "B5", list[1], workbook)
    _write_center(worksheet, "B6", list[2], workbook)
    _write_center(worksheet, "B7", list[3], workbook)
    _write_center(worksheet, "B8", list[4], workbook)
    _write_center(worksheet, "B9", list[5], workbook)
    _write_center(worksheet, "B10",list[6], workbook)
    _write_center(worksheet, "B11",list[7], workbook)
    _write_center(worksheet, "B12",list[8], workbook)
    _write_center(worksheet, "B13",list[9], workbook)
    _write_center(worksheet, "B14",list[10], workbook)
    _write_center(worksheet, "B15",list[11], workbook)
    _write_center(worksheet, "B16",list[12], workbook)
    _write_center(worksheet, "B17",list[13], workbook)

    dst= xlrd.open_workbook(file)
    sheet=dst.sheet_by_name("Sheet1")
    dstrows=dst.sheet_by_name("Sheet1").nrows
    #sheet.cell_value(i,j)
    #钟锦
    M=0
    for name in listname:
        M=M+1
        for i in range(dstrows):
            if sheet.cell_value(i,0)==name:
                _write_center(worksheet, "%s3"%listchar[M-1], name, workbook)
                _write_center(worksheet, "%s4"%listchar[M-1], sheet.cell_value(i,1), workbook)
                _write_center(worksheet, "%s5"%listchar[M-1], sheet.cell_value(i,2), workbook)
                _write_center(worksheet, "%s6"%listchar[M-1], sheet.cell_value(i,3), workbook)
                _write_center(worksheet, "%s7"%listchar[M-1], sheet.cell_value(i,4), workbook)
                _write_center(worksheet, "%s8"%listchar[M-1], sheet.cell_value(i,5), workbook)
                _write_center(worksheet, "%s9"%listchar[M-1], sheet.cell_value(i,6), workbook)
                _write_center(worksheet, "%s10"%listchar[M-1],sheet.cell_value(i,7), workbook)
                _write_center(worksheet, "%s11"%listchar[M-1],sheet.cell_value(i,8), workbook)
                _write_center(worksheet, "%s12"%listchar[M-1],sheet.cell_value(i,9), workbook)
                _write_center(worksheet, "%s13"%listchar[M-1],sheet.cell_value(i,10), workbook)
                _write_center(worksheet, "%s14"%listchar[M-1],sheet.cell_value(i,11), workbook)
                _write_center(worksheet, "%s15"%listchar[M-1],sheet.cell_value(i,12), workbook)
                _write_center(worksheet, "%s16"%listchar[M-1],sheet.cell_value(i,13), workbook)
                _write_center(worksheet, "%s17"%listchar[M-1],sheet.cell_value(i,14), workbook)
                _write_center(worksheet, "%s20"%listchar[M-1], name, workbook)
                _write_center(worksheet, "%s21"%listchar[M-1], sheet.cell_value(i,16), workbook)
                _write_center(worksheet, "%s22"%listchar[M-1], float(day*8)-float(sheet.cell_value(i,14)), workbook)
                LV='%.2f%%'%(float(sheet.cell_value(i,16))/(float(day*8)-float(sheet.cell_value(i,14)))*100)
                _write_center(worksheet, "%s23"%listchar[M-1], LV, workbook)
                print (u"----%s本月饱和度是%s----"%(name,LV))
                sleep(1)
    #第一列
    _write_center(worksheet, "A3", u"耗时总计(1月)", workbook)
    _write_center(worksheet, "A4", '=SUM(C4:T4)', workbook)
    _write_center(worksheet, "A5", '=SUM(C5:T5)', workbook)
    _write_center(worksheet, "A6", '=SUM(C6:T6)', workbook)
    _write_center(worksheet, "A7", '=SUM(C7:T7)', workbook)
    _write_center(worksheet, "A8", '=SUM(C8:T8)', workbook)
    _write_center(worksheet, "A9", '=SUM(C9:T9)', workbook)
    _write_center(worksheet, "A10",'=SUM(C10:T10)', workbook)
    _write_center(worksheet, "A11",'=SUM(C11:T11)', workbook)
    _write_center(worksheet, "A12",'=SUM(C12:T12)', workbook)
    _write_center(worksheet, "A13",'=SUM(C13:T13)', workbook)
    _write_center(worksheet, "A14",'=SUM(C14:T14)', workbook)
    _write_center(worksheet, "A15",'=SUM(C15:T15)', workbook)
    _write_center(worksheet, "A16",'=SUM(C16:T16)', workbook)
    _write_center(worksheet, "A17",'=SUM(A4:A16)', workbook)


    worksheet.merge_range('A19:A20', u"2017年度", define_format_H2)
    worksheet.merge_range('B19:B20', u"工作饱和度（团队）", define_format_H3)
    worksheet.merge_range('C19:T19', u"工作饱和度(18人-单人)", define_format_H3)
    _write_center(worksheet, "A21", u"%s月总工时"%m, workbook)
    _write_center(worksheet, "A22", u"总工时(工作日*8-休假)", workbook)
    _write_center(worksheet, "A23", u"饱和度", workbook)
    _write_center(worksheet, "B21", '=SUM(C21:T21)' , workbook)
    _write_center(worksheet, "B22", '=SUM(C22:T22)', workbook)
    _write_center(worksheet, "B23", '----', workbook)

    #写缺陷
    worksheet.merge_range('A26:A27', u"2017年度", define_format_H2)
    worksheet.merge_range('B26:O26', u"测试工程师缺陷度量（14人-单人）", define_format_H3)
    _write_center(worksheet, "A28",u"缺陷度量" , workbook)
    _write_center(worksheet, "A29",u"%s月个人bug总数"%m , workbook)
    _write_center(worksheet, "A30",u"日均测试时间(测试执行总时/8h)" , workbook)
    _write_center(worksheet, "A31",u"日均bug(bug总数/日均测试时间)", workbook)

    try:
        buglist=bug(file,filepath,m)
        dst1= xlrd.open_workbook(file)
        sheet1=dst1.sheet_by_name("Sheet1")
        dstrows1=dst1.sheet_by_name("Sheet1").nrows
        K=0
        for name in buglist:
            K=K+1
            _write_center(worksheet, "%s27"%listbugchar[K-1], name, workbook)
            _write_center(worksheet, "%s28"%listbugchar[K-1],u"日均Bug", workbook)
            for i in range(dstrows1):
                if sheet1.cell_value(i,0)==name:
                    _write_center(worksheet, "%s29"%listbugchar[K-1], sheet1.cell_value(i,15), workbook)
                    _write_center(worksheet, "%s30"%listbugchar[K-1], '%0.1f'%(float(sheet1.cell_value(i,5))/8), workbook)
                    _write_center(worksheet, "%s31"%listbugchar[K-1], '%0.1f'%(float(sheet1.cell_value(i,15)) * 8/(sheet1.cell_value(i,5))), workbook)
    except Exception,e:
        print e

    workbook.close()

#主程序执行程序
m=raw_input(u'请输入本年2017年工作日报月份：\n'.encode('gb18030'))
s=raw_input(u'请输入本年2017年%s月法定节假日天数：\n'.encode('gb18030')%(int(m)))
month=calend(int(m))-int(s)
print (u'本月一共有%s工作日（请假暂未计算）'.encode('gb18030')%month)
sleep(1)
print (u'请确保嵩恒产品研发管理平台bug表导出后另存.xlsx表（确保-Creator与Created两个字段）'.encode('gb18030'))
sleep(1)
filepath=raw_input(u'请拖入同级文件(测试组日报与bug表)父文件夹位置(确保-测试组工作日报与产品研发两个字段)：\n'.encode('gb18030'))
sleep(1)
filename=raw_input(u'请拖入生成报告的文件夹位置：\n'.encode('gb18030'))
sleep(1)

filepath=filepath+'\\'
file=filename+'\\'+"result.xls"
filereport=filename+'\\'+"report.xls"
#测试文件是否存在
testfileexists(file)
testfileexists(filereport)
#处理文件读表
alldir=eachFile(filepath)
for i in alldir:
    if u"测试组工作日报" in i:
        print i
        data=xlrd.open_workbook(i)
        sheetall=data.sheets()
        for j in sheetall:
            readexcel(j,file)

#处理生成的表空白写0
writealldata(file)
#写总表
writereport(filepath,file,filereport,m,month)
#计算表
#删除
os.remove(file)
print 'All OK'
while True:
    m=raw_input(u"输入Enter键退出程序：".encode('gb18030'))
    if not m:
        exit()
    else:
        sleep(3)


