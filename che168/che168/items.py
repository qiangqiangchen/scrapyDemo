# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Che168Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    #++++++++++++网页信息
    url=scrapy.Field()
    dealerid=scrapy.Field()
    infoid=scrapy.Field()
    #++++++++++++详细信息
    #标题
    car_title = scrapy.Field()
    #价格
    car_price = scrapy.Field()
    #行驶里程
    car_mileage = scrapy.Field()
    #首次上牌时间
    car_firstLicensed = scrapy.Field()
    #排量()
    car_displacement = scrapy.Field()
    #档位
    car_gearbox = scrapy.Field()
    #所在地
    car_location = scrapy.Field()
    #排放标准
    car_standard = scrapy.Field()
    #看车地点
    car_address = scrapy.Field()
    
    #++++++++++++基本信息
    #年检到期时间
    car_inspection_date = scrapy.Field()
    #保险到期时间
    car_insurance_date = scrapy.Field()
    #质保到期时间
    car_expiration_date = scrapy.Field()
    #过户次数
    Change_number = scrapy.Field()
    #用途
    use = scrapy.Field()
    #维护保养
    maintain = scrapy.Field()
    #商家名称
    dealerName = scrapy.Field()
    
    
    
    
    #++++++++++++车辆配置
    #发动机
    car_engine = scrapy.Field()
    #车辆级别
    car_level = scrapy.Field()
    #颜色
    car_color = scrapy.Field()
    #燃油标号
    car_fuel_type = scrapy.Field()
    #驱动方式
    car_drive_mode = scrapy.Field()
    
    #++++++++++++车辆配置
    #车辆图片
    car_image = scrapy.Field()
    
    pass
