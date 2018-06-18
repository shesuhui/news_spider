from scrapy.item import Item, Field


class Website(Item):

    name = Field()
    date = Field()
    url = Field()
