# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BoleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    
class newsItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    
class guideItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    
class basicItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
