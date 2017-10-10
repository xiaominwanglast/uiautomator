#coding:utf-8
import webbrowser
import time
import os
sogouPath = r'C:\Users\Administrator\AppData\Local\SogouExplorer\SogouExplorer.exe'            #  例如我的：C:\***\***\***\***\Google\Chrome\Application\chrome.exe
chromePath=r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))  #这里的'chrome'可以用其它任意名字，如chrome111，这里将想打开的浏览器保存到'chrome'
url='http://w3.shaqm.com/'
webbrowser.get('chrome').open(url,new=1,autoraise=True)
time.sleep(8)
from PIL import ImageGrab
im = ImageGrab.grab()
im.save('1.jpeg')
from PIL import Image
box=(0,0,1080/2,1920/10)
image=Image.open('1.jpeg')
newImage = image.crop(box)
newImage.save('1_1.jpeg')
task = 'taskkill /IM chrome.exe /F'
os.system(task)

import xlsxwriter
book = xlsxwriter.Workbook('pict.xlsx')
sheet = book.add_worksheet('demo')
sheet.insert_image('I2','1_1.jpeg')
sheet.insert_image('I14','1_1.jpeg')
sheet.insert_image('I26','1_1.jpeg')
book.close()