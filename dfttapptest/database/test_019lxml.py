#coding:utf-8
from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
#etree.parse('hello.html') 加载文档
html = etree.HTML(text)  #etree.HTML初始化
print type(html)
#result = etree.tostring(html,pretty_print=True) #转为内容
print html.xpath('//li') #获取所有根下li标签  类型为ElementTree
print html.xpath('//li/@class')  #获取 <li> 标签的所有 class 同级内容下
print etree.tostring(html.xpath('//li/a[@href="link3.html"]')[0]) #获取a标签里n内容
print etree.tostring(html.xpath('//li//span')[0]) #获取li标签下所有span标签内容,存在两层关系要用//
print html.xpath('//li/a//@class')  #a标签根下的属性为class的值
print html.xpath('//li[last()]/a/@href') #获取最后一个li标签下a标签的href属性内容
sss=etree.tostring(html.xpath('//li[last()-1]/a')[0]) #获取倒数第二个内容
print type(sss)
print etree.tostring(html.xpath('//*[@class="item-0"]')[0]) #获取根下所有class为这个的li整个内容