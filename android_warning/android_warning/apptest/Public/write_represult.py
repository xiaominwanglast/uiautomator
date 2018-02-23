#coding:utf-8
import os
import  xlrd
from xlutils.copy import copy
import  xlwt
from xlwt import *


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

def redmark():
    fnt= xlwt.Font()
    fnt.name= u"宋体"
    fnt.colour_index= 2
    fnt.height = 15*15
    fnt.bold= True
    style0= xlwt.XFStyle()
    style0.font= fnt
    return style0

def writefile(wrfile,content):
            #将执行失败的用例名写到excle中
        if os.path.exists(wrfile):
            pass
        else:
            w= xlwt.Workbook()
            w.add_sheet('Sheet1')
            w.save(wrfile)
            print (u"创建文件成功")

        rb = xlrd.open_workbook(wrfile)
        rows= rb.sheet_by_name("Sheet1").nrows

        wb=copy(rb)
        wb.get_sheet(0).write(rows,0,content[0])
        wb.get_sheet(0).write(rows,1,content[1])
        wb.get_sheet(0).write(rows,2,content[2])
        wb.get_sheet(0).write(rows,3,content[3])
        wb.save(wrfile)


#将包含有截图的excel文件与测试用例的case名对比，将有截图的用例名标为Fail
def writedata(srcfile,dstfile):
    if os.path.exists(srcfile):
        src = xlrd.open_workbook(srcfile)
        dst= xlrd.open_workbook(dstfile)

        wb=copy(dst)
        srcrows=src.sheet_by_name("Sheet1").nrows
        dstrows=dst.sheet_by_name("Android").nrows
        dstcols=dst.sheet_by_name("Android").ncols

#        print srcrows,dstrows,dstcols
        line=dst.sheet_by_name("Android")
        for i in range(1,dstrows):
            for j in range(srcrows):
                unit=line.cell(i,dstcols-1).value
                if(unit.split(',')[0]):
                    for z in range(0,len(unit.split(','))):
                        if str(unit.split(',')[z]).strip() == str(src.sheet_by_name("Sheet1").cell(j,0).value).strip():
                            writestr1=src.sheet_by_name("Sheet1").cell(j,1)
                            writestr2=src.sheet_by_name("Sheet1").cell(j,2)
                            wb.get_sheet(0).write(i,dstcols-3,writestr1.value)
                            wb.get_sheet(0).write(i,dstcols-2,writestr2.value)

        #保存文件
        wb.save(dstfile)
    else:
        print (u"需要创建excel文件")

def writeTestPass(dstfile):
    if os.path.exists(dstfile):
        dst= xlrd.open_workbook(dstfile)
        wb=copy(dst)
        dstrows=dst.sheet_by_name("Android").nrows
        dstcols=dst.sheet_by_name("Android").ncols
        pid=os.popen("netstat -ano|findstr 4723|findstr LISTENING").read().split()
        if pid:
            for i in range(1,dstrows):
                if (dst.sheet_by_name("Android").cell_value(i,dstcols-1)):
                    wb.get_sheet(0).write(i,dstcols-3,"Pass")
        else:
            for i in range(24,dstrows):
                if (dst.sheet_by_name("Android").cell_value(i,dstcols-1)):
                    wb.get_sheet(0).write(i,dstcols-3,"Pass")
        wb.save(dstfile)
    else:
        print (u"需要创建excel文件")

def writeSuperlink(dstfile,anyshare):
    if os.path.exists(dstfile):
        n= "HYPERLINK"
        dst=xlrd.open_workbook(dstfile)
        wb=copy(dst)
        dstrows=dst.sheet_by_name("Android").nrows
        dstcols=dst.sheet_by_name("Android").ncols
        for i in range(1,dstrows):
            if dst.sheet_by_name("Android").cell_value(i,dstcols-3)=="Fail":
                readstr=dst.sheet_by_name("Android").cell_value(i,dstcols-2)
                linkPath=anyshare+readpicturename(readstr)
                wb.get_sheet(0).write(i,dstcols-3,"Fail",redmark())
                wb.get_sheet(0).write_merge(i, i,dstcols-2, dstcols-2, xlwt.Formula(n +'("%s")'%linkPath),superlinkstyle())
            if dst.sheet_by_name("Android").cell_value(i,dstcols-3)=="Error":
                wb.get_sheet(0).write(i,dstcols-3,"Error",redmark())
        wb.save(dstfile)

def readpicturename(path):
    screen=""
    tap=path.split("\\")
    index=tap.index('screen')
    for i in range(index,len(tap)):
        screen=screen+"/"+tap[i]
    return screen


def writepass(failfile,passfile,dstfile):
    if os.path.exists(failfile):
        fa = xlrd.open_workbook(failfile)
        pa= xlrd.open_workbook(passfile)
        farows=fa.sheet_by_name("Sheet1").nrows
        parows=pa.sheet_by_name("Sheet1").nrows
        sun=0
        for i in range(parows):
            for j in range(farows):
                if pa.sheet_by_name("Sheet1").cell_value(i,0) == fa.sheet_by_name("Sheet1").cell_value(j,0):
                    sun=sun+1
            if sun==0:
                content=[pa.sheet_by_name("Sheet1").cell_value(i,0),"Pass"," "]
               # print pa.sheet_by_name("Sheet1").cell_value(i,0)
                writefile(dstfile,content)
       # os.remove(passfile)
    else:
        pa= xlrd.open_workbook(passfile)
        parows=pa.sheet_by_name("Sheet1").nrows
        for i in range(parows):
            content=[pa.sheet_by_name("Sheet1").cell_value(i,0),"Pass"," "]
            writefile(dstfile,content)
      #  os.remove(passfile)


'''
failfile=r"E:\wxm\pycharm\python\android_warning\apptest\result\excel\2016-12-28\FailureReport.xls"
passfile=r"E:\wxm\pycharm\python\android_warning\apptest\result\excel\2016-12-28\PassReport.xls"
dstfile=r"E:\wxm\pycharm\python\android_warning\apptest\result\excel\2016-12-28\RelPassReport.xls"
writepass(failfile,passfile,dstfile)
'''