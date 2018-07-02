# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.items import Website

from dirbot.poem import Poem

import scrapy

from scrapy_splash import SplashRequest



"""
抓取唐诗三百首
"""

           
class PoemSpider(Spider):
    name = "poem"
    allowed_domains = ["gushiwen.org"]
    start_urls = [
        "https://so.gushiwen.org/gushi/tangshi.aspx"
    ]


    # def start_requests(self): 
    #     for url in self.start_urls:
    #         yield SplashRequest(url,args = {'timeout':8,'images':0})

    def parse(self, response):

       
        sites = response.css('body > div.main3 > div.left > div.sons > div.typecont> span>a::attr(href)').extract()
        for site in sites:
            if site is not None and site is not '':
               # print("debugger info:"+next_page_url)
               detail_url=response.urljoin(site)
               yield scrapy.Request(detail_url,self.parse_paper,dont_filter=True)


    def parse_paper(self,response):
        # print("debugger info:"+response.meta['url'])
        poem=Poem()
        poem['title']=response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/h1/text()').extract_first()
        poem['author']=":".join(response.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/p/a/text()').extract())
        poem['content']="".join(response.xpath('/html/body/div[2]/div[1]/div[2]').css('div.contson::text').extract())
        poem['url']=response.url
        # print(paper)
        yield poem 



