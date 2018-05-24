# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XiaocaoPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,VideoItem):
            self.saveVideo(item)
        if isinstance(item,ForumItem):
            self.saveForum(item)
        if isinstance(item,PictureItem):
            self.savePicture(item)
        if isinstance(item,PhotoItem):
            self.savePhoto(item)
        if isinstance(item,TextItem):
            self.saveText(item)
        return item
    def saveVideo(item):
        pass
    def saveForum(item):
        pass
    def savePicture(item):
        pass
    def savePhoto(item):
        pass
    def saveText(item):
        pass