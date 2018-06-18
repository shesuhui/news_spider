# -*- coding: utf-8 -*-  
import random, base64  
from settings import PROXIES  
from settings import USER_AGENTS
  
class RandomUserAgent(object):
	def __init__(self,agnets):
		self.agnets=agnets

	@classmethod
	def from_crawler(cls,crawler):
		return cls(crawler.settings.getlist('USER_AGENTS'))

	def process_request(self,request,spider):
		user_agent=random.choice(USER_AGENTS)
		request.headers.setdefault('User-Agent',user_agent)


class ProxyMiddleware(object):  
    def process_request(self, request, spider):  
        proxy=random.choice(PROXIES)
        if proxy['user_pass'] is not None:
        	request.meta['proxy']="http://%s" % proxy['ip_port']
        	encoded_user_pass=base64.encodestring(proxy['user_pass'])
        	request.headers['Proxy-Authorization']='Basic'+encoded_user_pass
        	print "**************ProxyMiddleware have pass************" + proxy['ip_port']
        else:
        	print "**************ProxyMiddleware no pass************" + proxy['ip_port']
        	request.meta['proxy'] = "http://%s" % proxy['ip_port']

