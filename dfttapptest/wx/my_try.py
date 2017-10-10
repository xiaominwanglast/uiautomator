#coding:utf-8'
import sys,os
print sys.version_info
print sys.platform
import webbrowser
print os.path.join(os.getcwd(),'temp','wxqr.png')
webbrowser.open(os.path.join(os.getcwd(),'temp','E:\\wxm\\pycharm\\python\\dfttapptest\\wx\\temp\\wxqr.png'))
