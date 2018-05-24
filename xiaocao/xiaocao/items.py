# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaocaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class VideoItem(scrapy.Item):
    id=scrapy.Field()
    title=scrapy.Field()
    user_nick=scrapy.Field()
    creat_date=scrapy.Field()
    video_path=scrapy.Field()
    
class ForumItem(scrapy.Item):
    id=scrapy.Field()
    title=scrapy.Field()
    user_nick=scrapy.Field()
    creat_date=scrapy.Field()
    images=scrapy.Field()
    magnets=scrapy.Field()
    content=scrapy.Field()
    
class PictureItem(scrapy.Item):
    id=scrapy.Field()
    title=scrapy.Field()
    user_nick=scrapy.Field()
    creat_date=scrapy.Field()
    images=scrapy.Field()
    
class PhotoItem(scrapy.Item):
    id=scrapy.Field()
    title=scrapy.Field()
    user_nick=scrapy.Field()
    creat_date=scrapy.Field()
    images=scrapy.Field()
    
class TextItem(scrapy.Item):
    id=scrapy.Field()
    title=scrapy.Field()
    user_nick=scrapy.Field()
    creat_date=scrapy.Field()
    text=scrapy.Field()
    
