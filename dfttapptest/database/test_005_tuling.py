#coding:utf-8
import sys,requests,json
def succesion(info):
    appkey="e5ccc9c7c8834ec3b08940e290ff1559"
    url="http://www.tuling123.com/openapi/api?key=%s&info=%s"%(appkey,info)
    content=requests.get(url)
    answer=content.text
    ans=json.loads(answer)
    text=ans['text']
    return text

def main(info):
    info = info.decode('gbk').encode('utf-8')
    aa=succesion(info)
    print u'图灵:%s'%aa

if __name__ == '__main__':
    print u'----开始聊天吧----'.encode('gb18030')
    while True:
        info = raw_input(u'请询问：\n'.encode('gb18030'))
        if '88' in info:
            break
        main(info)
