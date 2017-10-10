#coding:utf-8
import xlrd,os
num=1
def run():
    for i in readlines():
        global num
        if 'text' in i:
            num=i.split('"')[0].split('(')[1].split(')')[0] #获取数值
        if num%2==0:
            fs=open(i,)  #i提取字符串（1）
            fs.write(i)


'''

def eachFile(filepath):
    dir=[]
    newdir=[]
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        dir.append(child.decode('gbk'))
    return dir

def dodata(i,filepath):
    data=xlrd.open_workbook(i)
    sheetpage=data.sheet_by_name('Sheet1')
    nrows=sheetpage.nrows
    ncols=sheetpage.ncols
    for i in range(1,nrows):
        datarow=[]
        txtpath=filepath+'map'+str(i)+'.txt'
        for j in range(ncols):
            datarow.append(sheetpage.cell_value(i,j))
            # cell_value值与文件做关联判断
        txtrun(datarow,txtpath,i)

def txtrun(datarow,txtpath,i):
    f = open(txtpath)
    lines=f.readlines()
    try:
        lines[18]='SEX: '+datarow[0]+'\n'
        lines[19]='AGE: '+datarow[1]+'\n'
        lines[20]='ACC: '+datarow[2]+'\n'
        lines[21]='ACT: '+datarow[3]+'\n'
        lines[22]='SCC: '+str(datarow[4])+'\n'
        print lines[22]
    except:
        print (u"第%s行数据%s存在异常,跳过此数据进行下一条数据处理"%(i,datarow))
    else:
        w = open(txtpath,'w')
        for k in lines:
            w.write(k.encode('gb18030'))
        w.close()

filepath='E:\\mac\\report\\'
alldir=eachFile(filepath)
print alldir

for i in alldir:
    if "test" in i:
        print i
        dodata(i,filepath)

'''
