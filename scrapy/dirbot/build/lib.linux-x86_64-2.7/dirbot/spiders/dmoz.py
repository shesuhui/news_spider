from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.items import Website


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
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
        "http://www.jcrb.com/legal/jj/index_24.html"
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

        for site in sites:
            item = Website()
            item['name'] = site.css('li>a::text').extract_first()
            item['url'] = site.css('li>a::attr(href)').extract_first()
            item['date'] = site.css('li::text').extract_first()
            items.append(item)

        return items
