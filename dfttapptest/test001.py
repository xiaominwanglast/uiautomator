#coding:utf-8

import xlrd
import xlwt
from xlutils.copy import copy
from xlwt import *
import os
from xlrd import cellname
def superlinkstyle():
    fnt = xlwt.Font()
    fnt.name = u"宋体"
    fnt.colour_index = 4
    fnt.bold = False
    fnt.height = 15*15  #设置字体大小
    fnt.underline = xlwt.Font.UNDERLINE_SINGLE  #设置下划线DOUBLE(双下划线),SINGLE(单下划线)
    style = xlwt.XFStyle()
    style.font = fnt
    return style
data = xlrd.open_workbook(r'E:\os\excel\2016-12-07\ResultReport.xls')
#table = data.sheets()[0] # 打开第一张表
cols=data.sheet_by_name("Android").ncols
nols=data.sheet_by_name("Android").nrows
sheet=data.sheet_by_name("Android")
n= "HYPERLINK"
print cols,nols
book=copy(data)
sheet1=book.get_sheet(0)
font0= xlwt.Font()
font0.colour_index= 2
font0.bold= False
h_style= XFStyle()
h_style.font=font0
a=u"AnyShare://头条移动端项目组/测试自动化实施/【东方头条】自动化ios&andriod实施版本-测试结果/未封版自动化回归/【东方头条】Android/【东方头条】android1.5.3版本包自动化回归/screen/nologin/news/2016-12-06/nologin_NewsStyle.test_01_style_12062039.png"
print type(a)
sheet1.write(1,7,"Fail",superlinkstyle())
for i in range(6):
    sheet1.write_merge(i, i,10, 10, xlwt.Formula(n +'("%s")'%a),superlinkstyle())

book.save(r"E:\os\excel\2016-12-07\ResultReport.xls")


'''
print table.cell(2,0).value
if table.cell(2,0).value:
    print table.cell(1,0).value
else:
    print 11
nologin_NewsStyle.test_01_style_12062039.png
aa=table.cell(1,0).value
print len(aa.split(',')),aa.split(',')[0]
bb=table.cell(0,0).value
cc=table.cell_value(2,0)
print cc.split(',')[0]
print bb
print len(bb.split(','))
print bb.split(',')[0]
print len(bb)

nrows = table.nrows # 获取表的行数
book=copy(data)
bs=book.get_sheet(0)
print "-----------------"
print table.cell_value(2,0)
if (table.cell_value(2,0)):
    print 1
else:
    print "OK"
for j in range(1,nrows):
    bs.write(j,4,"pass")
book.save('C:\\Users\\Administrator\\Desktop\\result\\test.xls')
import threading
import time
from appium import webdriver
import subprocess
import os
import xlrd
import xlwt
from xlutils.copy import copy
import os
from xlrd import cellname

dstfile=r"E:\wxm\pycharm\python\androidTest\apptest\config\ResultReport.xls"
dst= xlrd.open_workbook(dstfile)
wb=copy(dst)
dstrows=dst.sheet_by_name("Android").nrows
dstcols=dst.sheet_by_name("Android").ncols
for i in range(1,dstrows):
    if (dst.sheet_by_name("Android").cell_value(i,0)):
        wb.get_sheet(0).write(i,dstcols-2,"pass")
wb.save(dstfile)


#os.system('start startAppiumServer.bat')
#coding:utf-8
# 读取excel数据
# 小罗的需求，取第二行以下的数据，然后取每行前13列的数据
# How to write to an Excel using xlwt module


fail=xlrd.open_workbook(r'C:\Users\Administrator\Desktop\result\fail.xls')
failtable=fail.sheet_by_name("1")
failnrows=failtable.nrows

for j in range(0,nrows):
    for i in range(failnrows):
        rr=table.cell(j,0).value
        print rr
        if(rr.split(',')[0]):
            for m in range(0,len(rr.split(','))):
                print rr.split(',')[m]
                print "-----------------------"
                print failtable.cell(i,0).value
                if(rr.split(',')[m] ==failtable.cell(i,0).value):
                    bs.write(j,4,failtable.cell_value(i,1) )

book.save('C:\\Users\\Administrator\\Desktop\\result\\test.xls')
'''











'''

import xlwt
# 创建一个Workbook对象，这就相当于创建了一个Excel文件
book = xlwt.Workbook(encoding='utf-8', style_compression=0)

# 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
# 在电脑桌面右键新建一个Excel文件，其中就包含sheet1，sheet2，sheet3三张表
sheet = book.add_sheet('aa', cell_overwrite_ok=True)    # 其中的aa是这张表的名字

# 向表aa中添加数据
sheet.write(0, 0, 'EnglishName')    # 其中的'0, 0'指定表中的单元，'EnglishName'是向该单元写入的内容
sheet.write(1, 0, 'Marcovaldo')
txt1 = '中文名字'
sheet.write(0, 1, txt1.decode('utf-8')) # 此处需要将中文字符串解码成unicode码，否则会报错
txt2 = '马可瓦多'
sheet.write(1, 1, txt2.decode('utf-8'))

# 最后，将以上操作保存到指定的Excel文件中
book.save(r'e:\try1.xls') #在字符串前加r，声明为raw字符串，这样就不会处理其中的转义了。否则，可能会报错


t1=[]
data = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\result\fail.xls')
#table = data.sheets()[0] # 打开第一张表
table=data.sheet_by_name("1")
nrows = table.nrows # 获取表的行数
print nrows
for i in range(nrows): # 循环逐行打印
    if i == 0: # 跳过第一行
        continue
  #  print table.row_values(i)[:8] # 取前十三列
    t=table.row_values(i)[:1]
    if(t != [u'']):
        t1.append(t)
cell_value1 = table.cell_value(0, 0)
#print cell_value1
#print t1
#print t1[0]
book=copy(data)
bs=book.get_sheet(0)
for j in range(1,nrows):
    bs.write(j,4,"pass")
#bs.write(3,1,"aa")
book.save('C:\\Users\\Administrator\\Desktop\\result\\test.xls')

'''
