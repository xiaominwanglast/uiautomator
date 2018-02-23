#coding:utf-8
import xlsxwriter
import readconfig
import time
import xlrd
import os
from xlutils.copy import copy
# 设置居中
def get_format_center(wd,size):
    return wd.add_format({'align': 'left','valign': 'vcenter','font_size': size,'border':1})
# 写数据
def _write_center(worksheet, cl, data, wd):
    return worksheet.write(cl, data, get_format_center(wd,11))
def _write_data(worksheet, cl, data, wd):
    return worksheet.write(cl, data, get_format_center(wd,9))
def set_text_wrap(wd):
    return wd.add_format({}).set_text_wrap()
def readdst(dstfile):
    dst= xlrd.open_workbook(dstfile)
    dstrows=dst.sheet_by_name("Android").nrows
    dstcols=dst.sheet_by_name("Android").ncols
    num_all=0
    num_fail=0
    num_error=0
    num_pass=0
    for i in range(1,dstrows):
        if dst.sheet_by_name("Android").cell_value(i,dstcols-3):
            num_all=num_all+1
    for i in range(1,dstrows):
        if dst.sheet_by_name("Android").cell_value(i,dstcols-3)=="Fail":
            num_fail=num_fail+1
    for i in range(1,dstrows):
        if dst.sheet_by_name("Android").cell_value(i,dstcols-3)=="Error":
            num_error=num_error+1
    for i in range(1,dstrows):
        if dst.sheet_by_name("Android").cell_value(i,dstcols-3)=="Pass":
            num_pass=num_pass+1
    passpercent='%.2f%%'%(float(num_pass)/num_all*100)
    return dstrows-1,num_all,num_pass,num_fail,num_error,passpercent

def init(dstfile,report,start_time,end_time):
  #  workbook = xlsxwriter.Workbook(r'E:\os\excel\ResultReport.xls')
    workbook = xlsxwriter.Workbook(report)
    worksheet = workbook.add_worksheet(u"Android空白页预警")
    define_format_H2=workbook.add_format({'align': 'left','valign': 'vcenter','font_size':9,'border':1})
    define_format_H2.set_text_wrap()
    data=readdst(dstfile)
    #时间处理
    starttime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start_time))
    endtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time))
    # 设置列行的宽高
    worksheet.set_column("A:A", 14)
    worksheet.set_column("B:B", 16)
    worksheet.set_column("C:C", 14)
    worksheet.set_column("D:D", 16)
    worksheet.set_column("E:E", 14)
    worksheet.set_column("F:F", 16)
    worksheet.set_column("G:G", 23)
    worksheet.set_column("H:H", 35)
    for i in range(7):
        if i==0:
            worksheet.set_row(i, 20)
        worksheet.set_row(i, 17)

    define_format_H1 = workbook.add_format({'bold': 0, 'font_size': 15,'align':'center','border':1})
#    define_format_H2 = get_format(workbook, {'bold': 1, 'font_size': 14,'align':'center','bg_color':'blue','color':'#ffffff'})

    worksheet.merge_range('A1:F1', u"【东方头条】Android端自动化空白页预警测试报告", define_format_H1)
#    worksheet.merge_range('A2:F2', u"测试概括", define_format_H2)

    _write_center(worksheet, "A2", u"app名称", workbook)
    _write_center(worksheet, "A3", u"app版本号", workbook)
    _write_center(worksheet, "A4", u"网络", workbook)
    _write_center(worksheet, "A5", u"移动卡", workbook)
    _write_center(worksheet, "A6", u"测试机型号", workbook)
    _write_center(worksheet, "A7", u"测试机内存", workbook)

    _write_data(worksheet, "B2", readconfig.readappinstallmsg()[0], workbook)
    _write_data(worksheet, "B3", readconfig.readappinstallmsg()[1], workbook)
    _write_data(worksheet, "B4", readconfig.readsuminfo()[0], workbook)
    _write_data(worksheet, "B5", readconfig.readsuminfo()[1], workbook)
    _write_data(worksheet, "B6", readconfig.readsuminfo()[2], workbook)
    _write_data(worksheet, "B7", readconfig.readsuminfo()[3], workbook)


    _write_center(worksheet, "C2", u"平台", workbook)
    _write_center(worksheet, "C3", u"语言", workbook)
    _write_center(worksheet, "C4", u"自动化工具", workbook)
    _write_center(worksheet, "C5", u"自动化开始时间", workbook)
    _write_center(worksheet, "C6", u"自动化结束时间", workbook)
    _write_center(worksheet, "C7", u"运行时间", workbook)

    _write_data(worksheet, "D2", readconfig.readsuminfo()[4], workbook)
    _write_data(worksheet, "D3", readconfig.readsuminfo()[5], workbook)
    _write_data(worksheet, "D4", readconfig.readsuminfo()[6], workbook)
    _write_data(worksheet, "D5", starttime, workbook)
    _write_data(worksheet, "D6", endtime, workbook)
    _write_data(worksheet, "D7", time.strftime('%H-%M-%S',time.gmtime(end_time-start_time)).replace("-",":"), workbook)

    _write_center(worksheet,"E2",u"回归用例总数",workbook)
    _write_center(worksheet,"E3",u"目前执行总数",workbook)
    _write_center(worksheet,"E4",u"Pass总数",workbook)
    _write_center(worksheet,"E5",u"Fail总数",workbook)
    _write_center(worksheet,"E6",u"Error总数",workbook)
    _write_center(worksheet,"E7",u"Pass率",workbook)

    _write_data(worksheet, "F2", data[0], workbook)
    _write_data(worksheet, "F3", data[1], workbook)
    _write_data(worksheet, "F4", data[2], workbook)
    _write_data(worksheet, "F5", data[3], workbook)
    _write_data(worksheet, "F6", data[4], workbook)
    _write_data(worksheet, "F7", data[5], workbook)

    #关闭工作表
    workbook.close()
#dstfile=r"E:\wxm\pycharm\python\android_warning\apptest\result\excel\2016-12-22\ResultReport_warning.xls"
#report=r"E:\wxm\pycharm\python\android_warning\apptest\result\excel\2016-12-22\report.xls"
#init(dstfile,report,1481200719.349,1481271350.452)
