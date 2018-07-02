from scrapy.exceptions import DropItem
from poem import Poem
from es_pome import PoemType
from w3lib.html import remove_tags
import json
import codecs

class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    words_to_filter = ['politics', 'religion']

    def process_item(self, item, spider):
        for word in self.words_to_filter:
            if word in item['description'].lower():
                raise DropItem("Contains forbidden word: %s" % word)
        else:
            return item

class ElasticSearchPipeline(object):
    """es store"""
    def process_item(self,item,spider):
        if spider.name=='poem':
            es_poem=PoemType()
            es_poem.title=item['title']
            es_poem.author=item['author']
            es_poem.content=item['content']
            es_poem.url=item['url']
            es_poem.save()
            print("********success to save!")
        return item