# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from bole.items import newsItem,guideItem,basicItem

class BolePipeline(object):
    def process_item(self, item, spider):
        with open(r"E:\result.txt","a+") as f:
            #if isinstance(item,newsItem):
            #    f.write("newsItem: "+item['title']+"\n")
            if isinstance(item,guideItem):
                f.write("guideItem: "+item['title'+"\n"])
            #if isinstance(item,basicItem):
            #    f.write("basicItem: "+item['title']+"\n")
        return item
