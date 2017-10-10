#coding:utf-8
import os,xlrd
def testdirexists(dirpath):
    if (not os.path.exists(dirpath)):
        open(dirpath,'w')
def do(path):

    testdirexists(path)
    while True:
        data=[]
        os.popen('adb shell rm -rf sdcard/debug/clicklog_append.log')
        print '-----------------------------------------------------'
        a=raw_input(u'Enter(按回车键进行下一步测试，按y结束):\n'.encode('gb18030'))
        if a=='':
            os.popen('adb pull sdcard/debug/clicklog_append.log %s'%path)
            with open(path,'r') as f:
                txt=f.readlines()
            for i in txt:
                if 'code' in i:
                    a=i.split('\\')
                    if a[len(a)-1]=='tTQKB"\n':
                        data.append(a[8][1:])
            readdata(excelpath,data)
            f=open(path,'w')
            f.write('')
            f.close()
        if a=='y' or a=='Y':
            os.remove(path)
            break
def readdata(excelpath,data):
    if data==[]:
        print u'无click动作发生'
    else:
        print data
        lastclick=data[len(data)-1]
        print u'查找统计编号---%s'%lastclick
        src=xlrd.open_workbook(excelpath)
        sheet=src.sheet_by_name('Sheet1')
        srcn=sheet.nrows
        for i in range(srcn):
            try:
                if sheet.cell_value(i,2)==lastclick:
                    print "---"+sheet.cell_value(i,3).encode('gb18030')
                    print 'OK'
            except:
                pass

print u"###测试最后一次click对应的事件".encode('gb18030')
print u"###返回OK说明数据正常，没返回值异常".encode('gb18030')
excelpath=raw_input(u'请拖入按钮统计对照列表：\n'.encode('gb18030'))
path=os.path.dirname(excelpath)+'\\'+'log.txt'
do(path)
