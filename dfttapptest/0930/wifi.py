import time
import os
from adbUtils import ADB
import subprocess
def wifi():
    adb=ADB()
    subprocess.Popen('adb shell su&&svc wifi disable',stdout=subprocess.PIPE,shell=True)
    time.sleep(5)

  #  subprocess.Popen("adb shell su&&svc wifi enable",stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__=="__main__":
    wifi()