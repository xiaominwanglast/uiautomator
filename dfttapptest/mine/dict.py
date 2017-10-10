# coding=utf-8
from matplotlib import pyplot as plt
plt.figure()
places=[u'上海',u'北京',u'苏州',u'浙江']
sizes=[60,10,15,5]
plt.pie(sizes,explode=None,labels=places,colors=None,labeldistance=1.1,autopct='%3.1f%%',shadow=False,startangle=90,pctdistance=0.6)
plt.axis('equal')
plt.legend()
plt.show()