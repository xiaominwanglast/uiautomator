#coding:utf-8
import os
import time
import xlwt
import os
import zipfile
import shutil

'''
class defpath(object):
    work_path1=os.getcwd()+"\\result\\excel"
'''


def testdirexists(dirpath):
    if (not os.path.exists(dirpath)):
        os.makedirs(dirpath)
    else:
        print (u"目录已存在，不需要新建")


def testfileexists(filepath):

    if not os.path.exists(filepath):
        list1=filepath.split(',')
        for i in range(0,len(list1)):
            w= xlwt.Workbook()
            w.add_sheet('Sheet1')
            w.save(filepath[i])
            print (u"创建文件成功")

    else:
        print (u"excel文件已存在，不需要新建")


    #函数目的: 压缩指定目录为zip格式文件
    #参数说明：dirname为需要压缩的目录，zipfilename是期望压缩的文件路径名
def zip_dir(dirname,zipfilename):

    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))
                print name

    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        #print arcname
        zf.write(tar,arcname)
    zf.close()



def do_delfile(delfile):
    list1=delfile.split(',')
    for i in range(len(list1)):
        if os.path.exists(list1[i]):
            os.remove(list1[i])




def copy_files(listfilenames,dstdirname,dstfile):
    if (not os.path.exists(dstdirname)):
        os.makedirs(dstdirname)
    else:
        print (u"目录已存在，不需要新建")

    print len(listfilenames)
    for i in range(len(listfilenames)):
        print listfilenames[i]
        if os.path.isfile(listfilenames[i]):

            shutil.copy(listfilenames[i],dstfile)






'''
list1=os.getcwd()+"\config\FailureReport.xls"

print type(list1)
print list1.split(',')
copy_files(list1.split(','))
'''

'''
zip_dir(defpath.work_path1+'FailureReport.xls',defpath.work_path1+'11.zip')

list2=defpath.work_path1+'11.zip'
do_delfile(list2.split(','))

work_path1="E:\\wxm\\pycharm\\python\\android_warning\\apptest\\result\\excel"

zip_dir(work_path1,work_path1+"\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"_"+"report.zip")

'''