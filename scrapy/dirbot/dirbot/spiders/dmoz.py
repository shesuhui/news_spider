# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.items import Website

from dirbot.paper import Paper

import scrapy

from scrapy_splash import SplashRequest

                        
class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["jcrb.com"]
    start_urls = [
        "http://www.jcrb.com/legal/jj/index.html",
        "http://www.jcrb.com/legal/jj/index_1.html"
        # "http://www.jcrb.com/legal/jj/index_1.html",
        # "http://www.jcrb.com/legal/jj/index_2.html",
        # "http://www.jcrb.com/legal/jj/index_3.html",
        # "http://www.jcrb.com/legal/jj/index_4.html",
        # "http://www.jcrb.com/legal/jj/index_5.html",
        # "http://www.jcrb.com/legal/jj/index_6.html",
        # "http://www.jcrb.com/legal/jj/index_7.html",
        # "http://www.jcrb.com/legal/jj/index_8.html",
        # "http://www.jcrb.com/legal/jj/index_9.html",
        # "http://www.jcrb.com/legal/jj/index_10.html",
        # "http://www.jcrb.com/legal/jj/index_11.html",
        # "http://www.jcrb.com/legal/jj/index_12.html",
        # "http://www.jcrb.com/legal/jj/index_13.html",
        # "http://www.jcrb.com/legal/jj/index_14.html",
        # "http://www.jcrb.com/legal/jj/index_15.html",
        # "http://www.jcrb.com/legal/jj/index_16.html",
        # "http://www.jcrb.com/legal/jj/index_17.html",
        # "http://www.jcrb.com/legal/jj/index_18.html",
        # "http://www.jcrb.com/legal/jj/index_19.html",
        # "http://www.jcrb.com/legal/jj/index_20.html",
        # "http://www.jcrb.com/legal/jj/index_21.html",
        # "http://www.jcrb.com/legal/jj/index_22.html",
        # "http://www.jcrb.com/legal/jj/index_23.html",
        # "http://www.jcrb.com/legal/jj/index_24.html",
    ]


    def start_requests(self): #重新定义起始爬取点
        for url in self.start_urls:
            yield SplashRequest(url,args = {'timeout':8,'images':0})

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
       

        next_page_url=response.xpath('//*[@id="mainLeft"]/div[4]/a[8]/@href').extract_first()
        print('*********next_page_url******:'+next_page_url)
        if next_page_url is not None:
            next_page_url=response.urljoin(next_page_url)
            yield SplashRequest(next_page_url,callback=self.parse)
        # return items
        sites = response.css('#mainLeft > div.mainContent > ul > li')
        items = []
        for site in sites:
            detail_url=site.css('li>a::attr(href)').extract_first()
            if detail_url is not None and detail_url is not '':
               # print("debugger info:"+next_page_url)
               yield scrapy.Request(detail_url,self.parse_paper,meta={'url':detail_url}, dont_filter=True)


    def parse_paper(self,response):
        # print("debugger info:"+response.meta['url'])
        paper=Paper()
        paper['title']=response.xpath('//*[@id="mainLeft"]/h1/text()').extract_first()
        paper['author']=response.xpath('//*[@id="author_baidu"]/text()').extract_first()
        paper['source']=response.xpath('//*[@id="source_baidu"]/text()').extract_first()
        paper['date']=response.xpath('//*[@id="pubtime_baidu"]/text()').extract_first()
        paper['url']=response.meta['url']
        paper['content']=response.xpath('//*[@id="fontzoom"]/div/div').extract_first()
        # print(paper)
        yield paper



