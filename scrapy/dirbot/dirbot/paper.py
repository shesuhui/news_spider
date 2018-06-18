from scrapy.item import Item, Field

class Paper(Item):
	category=Field()
	title=Field()
	content=Field()
	images=Field()
	author=Field()
	source=Field()
	date=Field()
	url=Field()