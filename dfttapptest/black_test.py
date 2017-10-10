#coding:utf-8

from colorama import Fore, Back, Style

for color in ['GREEN', 'RED', 'BLUE']:
    print getattr(Fore, color), "It's color will be"
  #  print getattr(Back, color), "It's color will be", color
   # print Style.RESET_ALL