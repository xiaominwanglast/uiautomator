#coding:utf-8
import os
import subprocess
import platform
system = platform.system()

if "ANDROID_HOME" in os.environ:
    if system == "Windows":
        command = os.path.join(os.environ["ANDROID_HOME"], "platform-tools", "adb.exe")
    else:
        command = os.path.join(os.environ["ANDROID_HOME"], "platform-tools", "adb")
else:
    raise EnvironmentError(
        "Adb not found in $ANDROID_HOME path: %s." % os.environ["ANDROID_HOME"])

class ADB(object):

    def __init__(self, device_id = ""):
        if device_id == "":
            self.device_id = ""
        else:
            self.device_id = "-s %s" %device_id

    def shell(self,args):
        cmd = "%s %s shell %s" % (command,self.device_id, str(args))
        print cmd
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    def clearAppData(self,packageName):
        if "Success" in self.shell("pm clear %s" % packageName).stdout.read().splitlines():
            return "clear user data success "

        else:
            return "make sure package exist"


ADB().clearAppData("com.songheng.eastnews")

