#coding:utf-8

from time import strftime
from time import sleep
from PIL import Image


class screenshot(object):
    #进行截图操作，并指定截图的范围 box为指定的起始坐标
    def screencap(self,workpath,driver,box=(0,0,1080,1920),**kwargs):
        self.driver=driver
        self.workpath=workpath
        self.box=box

        dict1 = kwargs

        self.name = dict1['name']
        screencap_time = strftime("%Y-%m-%d %H_%M_%S-")
        tempfile=self.workpath+screencap_time + self.name + '.png'
        self.driver.get_screenshot_as_file(tempfile)
        sleep(2)

        #截图完之后，再保存具体的大小
        image=Image.open(tempfile)
        newImage = image.crop(box)
        newImage.save(tempfile)

        return screencap_time
