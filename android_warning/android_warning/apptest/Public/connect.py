#coding:utf-8
import time
from appium.webdriver.connectiontype import ConnectionType

#飞行模式
def connect_wifion(driver):
    driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
    time.sleep(6)
#关闭网络
def connect_noconnect(driver):
    driver.set_network_connection(ConnectionType.NO_CONNECTION)
    time.sleep(6)
#只打开wifi
def connect_onlywifi(driver):
    driver.set_network_connection(ConnectionType.WIFI_ONLY)
    time.sleep(8)
#只打开数据
def connect_onlydata(driver):
    driver.set_network_connection(ConnectionType.DATA_ONLY)
    time.sleep(6)
#数据wifi都打开
def connect_wifidataON(driver):
    driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
    time.sleep(6)
#返回显示状体
def webstate(driver):
    info = {0:"NO_CONNECTION",
            1:"AIRPLANE_MODE",
            2:"WIFI_ONLY",
            4:"DATA_ONLY",
            6:"ALL_NETWORK_ON"}
    state = driver.network_connection
    return info.get(state)

