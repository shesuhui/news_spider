from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.items import Website

from dirbot.paper import Paper

import scrapy

                        
class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["jcrb.com"]
    start_urls = [
        "http://www.jcrb.com/legal/jj/"
        "http://www.jcrb.com/legal/jj/index_1.html",
        "http://www.jcrb.com/legal/jj/index_2.html",
        "http://www.jcrb.com/legal/jj/index_3.html",
        "http://www.jcrb.com/legal/jj/index_4.html",
        "http://www.jcrb.com/legal/jj/index_5.html",
        "http://www.jcrb.com/legal/jj/index_6.html",
        "http://www.jcrb.com/legal/jj/index_7.html",
        "http://www.jcrb.com/legal/jj/index_8.html",
        "http://www.jcrb.com/legal/jj/index_9.html",
        "http://www.jcrb.com/legal/jj/index_10.html",
        "http://www.jcrb.com/legal/jj/index_11.html",
        "http://www.jcrb.com/legal/jj/index_12.html",
        "http://www.jcrb.com/legal/jj/index_13.html",
        "http://www.jcrb.com/legal/jj/index_14.html",
        "http://www.jcrb.com/legal/jj/index_15.html",
        "http://www.jcrb.com/legal/jj/index_16.html",
        "http://www.jcrb.com/legal/jj/index_17.html",
        "http://www.jcrb.com/legal/jj/index_18.html",
        "http://www.jcrb.com/legal/jj/index_19.html",
        "http://www.jcrb.com/legal/jj/index_20.html",
        "http://www.jcrb.com/legal/jj/index_21.html",
        "http://www.jcrb.com/legal/jj/index_22.html",
        "http://www.jcrb.com/legal/jj/index_23.html",
        "http://www.jcrb.com/legal/jj/index_24.html",
        # "http://www.jcrb.com/legal/zhuanti/",  
        # "http://www.jcrb.com/legal/redian/"
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sites = response.css('#mainLeft > div.mainContent > ul > li')
        items = []

        # for site in sites:
        #     item = Website()
        #     url= site.css('li>a::attr(href)').extract_first()
        #     if url is not None and url is not '':
        #         item['name'] = site.css('li>a::text').extract_first()
        #         item['url'] = site.css('li>a::attr(href)').extract_first()
        #         item['date'] = site.css('li::text').extract_first()
        #         items.append(item)
        for site in sites:
            next_page_url=site.css('li>a::attr(href)').extract_first()
            if next_page_url is not None and next_page_url is not '':
               # print("debugger info:"+next_page_url)
               item= scrapy.Request(next_page_url,self.parse_paper,meta={'url':next_page_url}, dont_filter=True)
               items.append(item)

        return items



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



