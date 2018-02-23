#coding:utf-8
import os
from PIL import Image
import sys
import time
sys.path.append (r"..")
import shutil

from apptest.PO import  BasePage
PATH = lambda p : os.path.abspath(p)
from apptest.Public.sendemail import smail



def refresh_page(driver,work_path1,name1,box):
       for i in range(1,3):
            BasePage.Base(driver).do_swipe(driver,"down")

                                 #如果不存在文件目录，就新建该文件夹
            if (not os.path.exists(work_path1)):
                os.makedirs(work_path1)

            if not os.listdir(work_path1):
                time.sleep(3)
                tempfile=work_path1+'image.png'
                driver.get_screenshot_as_file(tempfile)

                image=Image.open(tempfile)
                newImage = image.crop(box)
                newImage.save(tempfile)
            else:

#                name="nologin_refresh"
                name=name1
                stime=time.strftime('%m%d%H%M',time.localtime(time.time()))

                time.sleep(3)

                driver.get_screenshot_as_file(work_path1+name+stime+'.png')

                image=Image.open(work_path1+name+stime+'.png')
                newImage = image.crop(box)
                newImage.save(work_path1+name+stime+'.png')

                load=PATH("%s/%s.png" %(work_path1,name+stime))
                print load


                if (sameAs(load,"%s/image.png "%work_path1)):
                        body=u"信息流向下刷新-页面没有更新"
                        print ("图片相同".decode("utf-8"))

                #发送图片刷新后，没有更新的提示
                        smail().send_errormsg(str(name+stime+".png"),body,work_path1)
                        #发送完邮件后，删除该图片
                        os.remove("%s/%s.png"%(work_path1,name+stime))

                else:
                    print ("图片不同".decode("utf-8"))
            #删除文件
                    os.remove("%s/image.png "%work_path1)
            #将带时间戳的文件改为image.png名字
                    shutil.move("%s/%s.png" %(work_path1,name+stime),"%s/image.png "%work_path1)
        




#比较图片是否一致
def sameAs(loadImage,tempImage):
        """
        比较两张截图的相似度，完全相似返回True
        usage： load = loadImage("d:\\screen\\image.png")
                screen().subImage(100, 100, 400, 400).sameAs(load)
        """
        import math
        import operator

        image1 = Image.open(PATH("%s" %tempImage))
        image2 = Image.open(PATH("%s"%loadImage))


        histogram1 = image1.histogram()
        histogram2 = image2.histogram()

        differ = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2,  histogram1, histogram2)))/len(histogram1))
        if differ == 0:
            return True
        else:
            return False