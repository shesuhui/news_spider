from scrapy.item import Item, Field

class Poem(Item):
    title=Field()
    author=Field()
    content=Field()
    url=Field()