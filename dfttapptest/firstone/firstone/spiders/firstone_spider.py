#encoding=utf-8
import scrapy
import requests
from pymongo import MongoClient
from ..items import FirstoneItem
import smtplib
from email.mime.text import MIMEText
from .. import settings
import time
from scrapy.http import Request
from scrapy.spiders import Spider
class MaimaiSpider(Spider):
    #mongodb
    cn=MongoClient(settings.MONGODB_HOST,settings.MONGODB_PORT)
    db=cn[settings.MONGODB_DB]
    tb=db[settings.MONGODB_TABLE]

    name='baidunews'
    allowed_domains=['baidu.com']
    start_urls=['http://top.baidu.com/buzz?b=341']
    mainurl='http://top.baidu.com/'

    def parse(self, response):
        modes=response.xpath('//div[@class="hblock"]/ul/li/a/@href').extract()
        for mode in modes[1:]:
            news_type=response.xpath('//div[@class="hblock"]/ul/li[{}]/a/@title'.format(str(1+modes.index(mode)))).extract_first()
            yield Request(url=self.mainurl+mode[1:],callback=self.parse_item,meta={'news_type':news_type})

    def parse_item(self,response):
        bodys=response.xpath('//table[@class="list-table"]/tr')
        for body in bodys:
            if body.xpath('.//td[@class="first"]').extract():
                items=FirstoneItem()
                num=body.xpath('.//td[@class="first"]/span/text()').extract_first()
                title=body.xpath('.//td[@class="keyword"]/a/text()').extract_first()
                href=body.xpath('.//td[@class="keyword"]/a/@href').extract_first()
                focus_num=body.xpath('.//td[@class="last"]/span/text()').extract_first()
                items['num']=num
                items['_id']=title
                items['news_type']=response.meta['news_type']
                items['baidu_url']=href
                items['focus_num']=focus_num
                yield items

             #   print response.meta['news_type'].encode('gb18030'),num,title.encode('gb18030'),href


    def close(self, reason):
        if reason=='finished':
            header='<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head><table border="0" cellspacing="0" cellpadding="3" align="left" >'
            tail='</table></body></html>'
            line=''
            for data in self.tb.find():
                if int(data['num'])<=3:
                    tp0='<tr align="left"><td colspan="6">%s</td></tr>'%('*'*10)
                    tp1='<tr align="left"><td colspan="6">%s</td></tr>'%data['news_type']
                    tp2='<tr align="left"><td colspan="6">%s</td></tr>'%data['num']
                    tp3='<tr align="left"><td colspan="6">%s</td></tr>'%data['_id']
                    tp4='<tr align="left"><td colspan="6">%s</td></tr>'%data['baidu_url']
                    line=line+tp0+tp1+tp2+tp3+tp4
            body=header+line+tail
            msg = MIMEText(body,'html', 'utf-8')
            msg["Subject"] = "[%s]BaiduTopNews"%time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            msg["From"]    = settings.email_From
            msg["To"]      = ','.join(settings.email_To)
            try:
                s = smtplib.SMTP_SSL(settings.smtpHost, settings.smtpPort)
                s.login(settings.email_From,settings.email_pwd)
                s.sendmail(settings.email_From, msg["To"], msg.as_string())
                s.quit()
                print "Success!"
            except smtplib.SMTPException,e:
                print "sendemail_Falied,the reson is %s"%e