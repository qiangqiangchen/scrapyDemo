# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import log
from che168.DBHelper import DBHelper
from che168.items import Che168Item
from scrapy.exceptions import DropItem

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Che168Pipeline(object):
    def __init__(self):
        self.db=DBHelper()
    def process_item(self, item, spider):
        if self.is_exist(item):
            raise DropItem("title is exist ")
        else:
            sql="insert into che(dealerid,infoid,url,car_title,car_price,car_mileage,car_firstLicensed,car_displacement,car_gearbox,car_location,car_standard,car_address,car_inspection_date,car_insurance_date,car_expiration_date,Change_number,car_use,maintain,dealerName,car_engine,car_level,car_color,car_fuel_type,car_drive_mode,car_image) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"%(item['dealerid'],item['infoid'],item['url'],item['car_title'],item['car_price'][1:],item['car_mileage'][:-3],item['car_firstLicensed'],item['car_displacement'].split('／')[-1],item['car_gearbox'],item['car_location'],item['car_standard'],item['car_address'],item['car_inspection_date'],item['car_insurance_date'],item['car_expiration_date'],item['Change_number'],item['use'],item['maintain'],item['dealerName'],item['car_engine'],item['car_level'],item['car_color'],item['car_fuel_type'],item['car_drive_mode'],','.join(item['car_image'])
            )
            sql = sql.encode('utf-8')
            log.msg("sql : %s"%sql,level=log.DEBUG)
            self.db.insert(sql)
        
        return item
    def is_exist(self,item):
        select_sql="select * from che where infoid='%s';"%(item['infoid'])
        data=self.db.select(select_sql.encode('utf-8'))
        if data:
            log.msg("data is exist infoid : %s"%item['infoid'],level=log.DEBUG)
            return True
        return False
    
