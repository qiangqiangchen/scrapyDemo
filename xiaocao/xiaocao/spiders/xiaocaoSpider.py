# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
from xiaocao.items import VideoItem,ForumItem,PictureItem,PhotoItem,TextItem

class xiaocaoSpider(CrawlSpider):
    name="xiaocao"
    allowed_domains=["bc.postcc.us"]
    start_urls=["http://bc.postcc.us/index.php"]
    rules=[
        Rule(LinkExtractor(allow=(r'thread0806php\?fid=(22|7|8|16|20)',)),follow=True),
        Rule(LinkExtractor(allow=(r'htm_data/22/\d{4}/\d{7}.html',)),follow=True,callback='parse_video'),
        Rule(LinkExtractor(allow=(r'htm_data/7/\d{4}/\d{7}.html',)),follow=True,callback='parse_forum'),
        Rule(LinkExtractor(allow=(r'htm_data/8/\d{4}/\d{7}.html',)),follow=True,callback='parse_picture'),
        Rule(LinkExtractor(allow=(r'htm_data/16/\d{4}/\d{7}.html',)),follow=True,callback='parse_photo'),
        Rule(LinkExtractor(allow=(r'htm_data/20/\d{4}/\d{7}.html',)),follow=True,callback='parse_text'),
    ]
    
    def parse_video(self,response):
        pass
    def parse_forum(self,response):
        pass
    def parse_picture(self,response):
        pass
    def parse_photo(self,response):
        pass
    def parse_text(self,response):
        pass