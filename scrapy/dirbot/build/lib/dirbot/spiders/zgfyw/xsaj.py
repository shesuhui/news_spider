# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.items import Website

from dirbot.paper import Paper

import scrapy

import sys 

#解决打印中文注释错误
reload(sys) 
sys.setdefaultencoding('utf8')

#刑事案件.  https://www.chinacourt.org/article/index/id/MzAwNDAwAiPCAAA%3D.  page 1363


class XsajSpider(Spider):
	name="zgfyw-xsaj"
	
	
	start_urls=[
    	"https://www.chinacourt.org/article/index/id/MzAwNDAwAiPCAAA%3D"
	]


	

	def __init__(self):
		self.domain="https://www.chinacourt.org"
		self.start_page="https://www.chinacourt.org/article/index/id/MzAwNDAwAiPCAAA%3D"
	
	def parse(self,response):
		items=[]
		#msaj
		for i in range(21,50):
			page_url=self.start_page+"/page/"+str(i)+".shtml"
			print "********列表页面********"+page_url
			item=scrapy.Request(page_url,self.parse_pageList)
			items.append(item)	
		return items


	def parse_pageList(self,response):
		list_url=response.xpath('//*[@id="articleList"]/ul/li/span[1]/a/@href').extract()
		for detail_url in list_url:
			#print detail_url
			print "***********************正在爬取文章列表*************："+self.domain+detail_url
 			yield scrapy.Request(self.domain+detail_url,self.parse_detail,meta={'url':self.domain+detail_url})



	def parse_detail(self,response):
		paper=Paper()
		paper['category']='刑事案件'
		paper['title']=response.xpath('//*[@id="detail"]/div[2]/div[2]/text()').extract_first()
		paper['author']='中国法院网'
		paper['source']='中国法院网'
		paper['date']=response.xpath('//*[@id="detail"]/div[3]/span/text()').extract_first()
		paper['url']=response.meta['url']
		paper['content']=response.xpath('//*[@id="detail"]/div[4]/text()').extract_first()
		yield paper