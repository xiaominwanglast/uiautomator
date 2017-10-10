#coding:utf-8
import xlrd

def readurl(inter):
    url_path='E:\\wxm\\pycharm\\python\\1.7.0interandroid\\apptest\\config\\inter_url.xls'
    wk=xlrd.open_workbook(url_path)
    sheet=wk.sheet_by_name('Sheet1')
    for i in range(1,sheet.nrows):
      print sheet.cell_value(i,2)
      if sheet.cell_value(i,2).strip()==inter:
         return sheet.cell_value(i,4).strip()
if __name__=='__main__':
   inter='collection/newcol/singleimport'
   print readurl(inter)