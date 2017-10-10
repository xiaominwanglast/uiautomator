# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
from scrapy import signals
import random,base64,datetime,codecs
class ProxyMiddleware(object):
    agents = [
    "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",]
    proxyList = ['94.177.232.69:1189', '220.166.96.90:82', '77.81.226.124:1189', '198.50.219.239:8080', '166.111.77.32:80']
    def process_request(self, request, spider):
        pro_adr = random.choice(self.proxyList)
 #       print "USE PROXY -> "+pro_adr
  #      request.meta['proxy'] = "http://"+ pro_adr
        agent = random.choice(self.agents)
        print 'USE HEADERS ->'+agent
        request.headers["User-Agent"] = agent
        '''这里用的免费代理,不用用户名密码的.如果有用户名和密码,还要加入以下代码
        proxy_user_pass = "USERNAME:PASSWORD"
        encoded_user_pass = base64.encodestring(proxy_user_pass)
        request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass'''

    def process_response(self, request, response, spider):
        if response.status >= 400:
            reason = response.status_message(response.status)
            self._faillog(request, u'HTTPERROR',reason, spider)
        return response

    def process_exception(self, request, exception, spider):
        proxy=request.meta['proxy']
        print proxy
        self._faillog(request, u'EXCEPTION', exception, spider)
        return request

    def _faillog(self, request, errorType, reason, spider):
        with codecs.open('faillog.log', 'a', encoding='utf-8') as file:
            file.write("%(now)s [%(error)s] %(url)s reason: %(reason)s \r\n" %
                       {'now':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'error': errorType,
                        'url': request.url,
                        'reason': reason.encode('gbk')})

