#coding:utf-8
from bs4 import BeautifulSoup
import bs4,re
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
#soup = BeautifulSoup(open('index.html')) #打开文件路径
soup=BeautifulSoup(html,'lxml')  #lxml速度高，html.parser
#print soup.prettify()  #格式化样式输出
####Tag
#-------------------Tag 标签，两个重要的属性 name，attrs
print soup.title #输出tag标签为title的内容
#print soup.head #输出tag标签的head的内容
#print soup.a #只输出第一个tag
print soup.p.children

print type(soup.a) #类型为bs4.element.Tag
#属性1，name
print soup.name,soup.title.name #内部标签为本身的名字
#属性2，attrs
print soup.a.attrs #输出为字典形式内容的头文件
print soup.a.attrs.keys()
print soup.a['href'],soup.a.attrs['href'],soup.a.get('href') #同样的输出keys,字典的get value属性
#属性修改  字典内容的修改 或者del删除字典内容
print '--------------------------------------'
#--------------------NavigableString
print soup.p.string  #获取内容的方法
print type(soup.p.string) #类型为bs4.element.NavigableSring
print '-------------------------------------'
#--------------------BeautifulSoup
print type(soup.name),soup.name,soup.attrs #空字典

#-------------------Comment
print soup.a.string,type(soup.a.string)
if type(soup.a.string)== bs4.element.Comment:  #判断输出类型但是不能打印出输出内容
    print soup.a.string
#----------------------------------------------------
print u'遍历树--------------------------------------------'
####遍历
#--------------------直接子节点 .contents,.children
print soup.head.contents[0] #.contents输出是以list列表形式
print soup.head.children #list生成器对象
#for child in soup.body.children:  #遍历输出child结果
  #  print child
#-------------------所有子孙节点 .descendants 属性
#for child in soup.descendants:  #所有子节点递归打印
 #   print child
#-------------------节点内容 .string属性
print soup.head.string
print soup.title.string  #输出节点内容
#-------------------多个内容 .strings  .stripped_strings 属性
for string in soup.stripped_strings:  #遍历输出多个内容 #stripped去空格空行
    print string
print '---------------------------'
#-------------------父节点 .parent 属性
print soup.p.parent.name
#-------------------全部父节点 .parents 属性
for parent in soup.head.title.string.parents: #遍历父节点
    print parent.name
print '----------------------------'
#####搜索文档树
#----------------------find_all(name , attrs , recursive , text , **kwargs ) #当前tag的子节点tag
###name属性--字符串
#---------------------
print soup.find_all('b')
print soup.find_all('a')  #list列表
#--------------------
###name属性--正则
for tag in soup.find_all(re.compile(r'^b')):
    print tag
print '----------------------------'
###name属性--传列表
print soup.find_all(['a','b'])
###name属性--传True
for tag in soup.find_all(True):
    print tag.name
print '---------------------------'
###name属性--传方法
###2）keyword 参数
print soup.find_all(id='link1') #指定id时及搜索id
print soup.find_all(href=re.compile(r'^(http:)'))
print soup.find_all(href=re.compile("elsie"), id='link1') #指定多个tag属性
print'-------------------------'
#有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性
#data_soup = BeautifulSoup('<div data-foo="value">foo!</div>','lxml')
#print data_soup.find_all(attrs={'data-foo':"value"}) #data-*类型用attrs
###3）text 参数
print soup.find_all(text=["Tillie", "Elsie", "Lacie"]) #匹配正文内容
print soup.find_all(text=re.compile("Dormouse"))
###4）limit 参数
print soup.find_all('a',limit=2)
#------------------------find( name , attrs , recursive , text , **kwargs )
#它与 find_all() 方法唯一的区别是 find_all() 方法的返回结果是值包含一个元素的列表,而 find() 方法直接返回结果
#CSS选择器  标签名不加任何修饰，类名前加点，id名前加 #   soup.select()，返回类型是 list
#（1）通过标签名查找
print soup.select('a')
print soup.select('.sister')  #类加.
print soup.select('#link1') # id加#
print soup.select('p #link2') #组合查找
print soup.select('a[class="sister"]') #属性查找