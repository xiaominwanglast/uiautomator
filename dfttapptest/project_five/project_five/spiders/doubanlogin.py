#coding:utf-8
import scrapy
from scrapy.http import Request,FormRequest
import urllib2,urllib
import webbrowser

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['douban.com']
    #start_urls = ['http://douban.com/']
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}

    def start_requests(self):
        return [FormRequest("https://accounts.douban.com/login",headers=self.header,meta={"cookiejar":1},callback=self.parse)]

    def parse(self, response):
        captcha = response.xpath("//img[@id='captcha_image']/@src").extract_first()
        id=response.xpath('//input[@name="captcha-id"]/@value').extract_first()
        print id
        if captcha:
            print(u"此时有验证码.")
            localpath = "E:\\0930\\captcha.png"
            urllib.urlretrieve(captcha,filename=localpath)
            webbrowser.open(localpath)
            captchar_value=raw_input(u"查看验证码是:")
            return [FormRequest.from_response(response,
                                                  meta={'cookiejar': response.meta['cookiejar']},
                                                  headers=self.header,
                                                  formdata={
                                                      'source':'None',
                                                      'form_email': '18301924915',
                                                      'form_password': 'wang12345',
                                                      'captcha-solution': captchar_value,
                                                      'captcha-id': id,
                                                      'user_login': u'登录',
                                                      'redir':'https://www.douban.com/'
                                                  },
                                                  callback=self.after_login,
                                                  dont_filter=True)]
        else:
            return [FormRequest.from_response(response,meta={'cookiejar': response.meta['cookiejar']},headers=self.header,
                                              formdata={
                                                      'source': 'None',
                                                      'form_email': '18301924915',
                                                      'form_password': 'wang12345',
                                                      'user_login': u'登录',
                                                      'redir':'https://www.douban.com/people/163088717/'
                                                  },
                                                  callback=self.after_login,
                                                  dont_filter=True)]


    def after_login(self, response):
        print response.xpath('//title/text()').extract_first()