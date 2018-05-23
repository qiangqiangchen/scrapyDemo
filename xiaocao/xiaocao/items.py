# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaocaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    video = scrapy.Field()
    forum = scrapy.Field()
    picture = scrapy.Field()
    photo = scrapy.Field()
    pass
