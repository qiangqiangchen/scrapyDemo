# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
from bole.items import newsItem,guideItem,basicItem
import sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

class boleSpider(CrawlSpider):
    name="bole"
    allowed_domains=["python.jobbole.com"]
    start_urls=["http://python.jobbole.com//"]
    rules=[
        Rule(LinkExtractor(allow=(r'category/news',)),follow=True,callback='parse_news'),
        Rule(LinkExtractor(allow=(r'category/basic',)),follow=True,callback='parse_basic'),
        Rule(LinkExtractor(allow=(r'category/guide',)),follow=True,callback='parse_guide'),
    ]
    def parse_news(self,response):
        self.log('===>url:%s'%response.url)
        items=newsItem()
        news=response.xpath('//a[@class="archive-title"]')
        for new in news:
            items['url']=new.xpath('./@href').extract()[0]
            items['title']=new.xpath('./@title').extract()[0]
            yield items
    def parse_basic(self,response):
        self.log('===>url:%s'%response.url)
        items=basicItem()
        basic=response.xpath('//a[@class="archive-title"]')
        for b in basic:
            items['url']=b.xpath('./@href').extract()[0]
            items['title']=b.xpath('./@title').extract()[0]
            yield items
    def parse_guide(self,response):
        self.log('===>url:%s'%response.url)
        items=guideItem()
        guide=response.xpath('//a[@class="archive-title"]')
        for g in guide:
            items['url']=g.xpath('./@href').extract()[0]
            items['title']=g.xpath('./@title').extract()[0]
            yield items