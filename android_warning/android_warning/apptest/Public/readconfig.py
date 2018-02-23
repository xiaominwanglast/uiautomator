#coding:utf-8

import ConfigParser
import os
import shutil


#读取appconfig.ini 中的packname、appActivity项
def readappconfig():

    config = ConfigParser.ConfigParser()
    filejudge=os.path.dirname(os.getcwd())
    while True:
        if os.path.exists(filejudge+"\\config\\appconfig.ini"):
            break
        else:
            filejudge=os.path.dirname(filejudge)


    with open(filejudge+"\\config\\appconfig.ini","r") as cfgfile:
        config.readfp(cfgfile)
        packname=config.get("app","packname")
        appActivity=config.get("app","appActivity")
#    print smtpHost,smtpPort,sslPort,fromMail,username,password,toMail,cc
    return packname,appActivity




#读取appconfig.ini 中的packname、installname项
def readappinstallmsg():
    config = ConfigParser.ConfigParser()
    filejudge=os.path.dirname(os.getcwd())
    while True:
        if os.path.exists(filejudge+"\\config\\appconfig.ini"):
            break
        else:
            filejudge=os.path.dirname(filejudge)

    with open(filejudge+"\\config\\appconfig.ini","r") as cfgfile:
        config.readfp(cfgfile)
        packname=config.get("appinstall","packname")
        installname=config.get("appinstall","installname")


#    print smtpHost,smtpPort,sslPort,fromMail,username,password,toMail,cc
    return packname,installname

#修改当前App版本号
def setappVersion(name):
    config = ConfigParser.ConfigParser()
    filejudge=os.path.dirname(os.getcwd())
    while True:
        if os.path.exists(filejudge+"\\config\\appconfig.ini"):
            break
        else:
            filejudge=os.path.dirname(filejudge)

    with open(filejudge+"\\config\\appconfig.ini","r") as cfgfile:
        config.readfp(cfgfile)
        config.set("appinstall", "installname", "touTiao_v"+name)
        installname=config.get("appinstall","installname")
        config.write(open(filejudge+"\\config\\appconfig.ini", "w"))
    return installname

#读取appconfig.ini 中的packname、installname项
def readsuminfo():
    config = ConfigParser.ConfigParser()
    filejudge=os.path.dirname(os.getcwd())
    while True:
        if os.path.exists(filejudge+"\\config\\appconfig.ini"):
            break
        else:
            filejudge=os.path.dirname(filejudge)

    with open(filejudge+"\\config\\appconfig.ini","r") as cfgfile:
        config.readfp(cfgfile)
        web=config.get("suminfo","web")
        mobile=config.get("suminfo","mobile")
        mobile_model=config.get("suminfo","mobile_model")
        memory=config.get("suminfo","memory")
        platform=config.get("suminfo","platform")
        language=config.get("suminfo","language")
        autotool=config.get("suminfo","autotool")
    sum=[web,mobile,mobile_model,memory,platform,language,autotool]
    return sum

def  readscheconfig():
    config = ConfigParser.ConfigParser()
    filejudge=os.path.dirname(os.getcwd())
    while True:
        if os.path.exists(filejudge+"\\config\\config.ini"):
            break
        else:
            filejudge=os.path.dirname(filejudge)

    with open(filejudge+"\\config\\config.ini","r") as cfgfile:
        config.readfp(cfgfile)
        start_minute=config.get("time","start_minute")
        start_hour=config.get("time","start_hour")

    return start_minute,start_hour

def removeall(rootdir):
    filelist=os.listdir(rootdir)
    for f in filelist:
        filepath = os.path.join( rootdir, f )
        if os.path.isfile(filepath):
            os.remove(filepath)
            print filepath+" removed!"
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath,True)
            print "dir "+filepath+" removed!"


