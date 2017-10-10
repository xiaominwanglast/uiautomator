#coding:utf-8
import os
import adbUtils

print adbUtils.ADB().getCurrentActivity()
print adbUtils.ADB().getCurrentPackageName()



'''
import zipfile
def zip_dir(dirname,zipfilename):

    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))
      #          print name

    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        print tar
        arcname = tar[len(dirname)+1:]
        print arcname
        zf.write(tar,arcname)

    zf.close()

'''












'''
print u"压缩操作 zip"
#获取当前目录树
fileLists=[]
for root,dirs,files in os.walk("E:\\0930"):
    for name in dirs:
        fileLists.append(os.path.join(root, name)) #目录入列表
#创建压缩文件
file2=zipfile.ZipFile(os.getcwd()+"/zipfile_module2"+".zip",'w',zipfile.ZIP_DEFLATED) #zipfile.zlib.DEFLATED 亦可
#写入目录树
for name in fileLists:
    file2.write(name)
#关闭压缩文件
file2.close()
'''