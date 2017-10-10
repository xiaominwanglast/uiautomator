#coding:utf-8
import xlrd
from pymongo import MongoClient
from xlutils.copy import copy
list1=[]
list2=[]
def write_data(data1,data2,data3):
    list1.append(data2)
    list2.append(data3)
    '''
    f=xlrd.open_workbook(path)
    sheet=f.sheet_by_name(u'统计总览')
    src=copy(f)
    row=sheet.nrows
    src.get_sheet(0).write(row,0,data1)
    src.get_sheet(0).write(row,1,data2)
    src.get_sheet(0).write(row,2,data3)
    src.save(path)
    '''

if __name__=='__main__':
    path=u'E:\\趣头条链接变化表20170615-01.xlsx'
    cn=MongoClient('127.0.0.1',27017)
    db=cn.qutoutiao
    table=db.result_other
    for dic_data in table.find():
        write_data(dic_data['url'],dic_data['first_domain'],dic_data['second_domain'])
    print  len(list(set(list1)))
    print  len(list(set(list2)))