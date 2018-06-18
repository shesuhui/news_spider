from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.items import Website

from dirbot.paper import Paper

import scrapy

"""
mingzhuyufazhi spider

"""

class PufaSpider(Spider):
	name="mzyfz-lifa"
	start_urls=[
    	"http://www.mzyfz.com"
	]
	
	def parse(self,response):
		items=[]
		for i in range(2,9):
			page_url="http://www.mzyfz.com/cms/faxunkuaibao/xinwenkuaibao/zhengfadongtai/html/1049/list-"+str(i)+".html"
			item=scrapy.Request(page_url,self.parse_pageList)
			items.append(item)

		page_url='http://www.mzyfz.com/cms/faxunkuaibao/xinwenkuaibao/zhengfadongtai/html/1049/'
		item=scrapy.Request(page_url,self.parse_pageList)
		items.append(item)
		return items


	def parse_pageList(self,response):
		list_url=response.xpath("/html/body/div[10]/div[1]/div[1]/div[2]/ul/li/a/@href").extract()
		for detail_url in list_url:
 			yield scrapy.Request(detail_url,self.parse_detail,meta={'url':detail_url})



	def parse_detail(self,response):
		paper=Paper()
		paper['title']=response.xpath('/html/body/div[10]/div[1]/div[1]/text()').extract_first()
		paper['author']=response.xpath('/html/body/div[10]/div[1]/div[2]/text()').extract_first()
		paper['source']=response.xpath('/html/body/div[10]/div[1]/div[2]/text()').extract_first()
		paper['date']=response.xpath('/html/body/div[10]/div[1]/div[2]/text()').extract_first()
		paper['url']=response.meta['url']
		paper['content']=response.xpath('//*[@id="maincontent"]').extract_first()
		yield paper