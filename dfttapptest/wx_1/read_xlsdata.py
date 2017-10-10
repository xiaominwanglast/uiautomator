#coding:utf-8
import xlrd
from xlutils.copy import copy
def read():
    fs=xlrd.open_workbook(path)
    sheet=fs.sheet_by_name(u'微信打开分享后重定向链接表')
    data_list=[]
    print sheet.nrows
    for i in range(1,sheet.nrows):
        if sheet.cell_value(i,1) not in data_list:
            data_list.append(sheet.cell_value(i,1))
    return len(data_list),data_list


if __name__=='__main__':
    path=u'E:\\趣头条链接变化表20170615-01.xlsx'
    data=read()
    for i in data[1]:
        f=xlrd.open_workbook(path)
        sheet=f.sheet_by_name('Sheet1')
        src=copy(f)
        row=sheet.nrows
        src.get_sheet(0).write(row,0,i)
        src.save(path)