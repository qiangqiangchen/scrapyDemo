# -*- coding:utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
import scrapy
from che168.items import Che168Item

base_url='https://www.che168.com/xian/a0_0msdgscncgpi1ltocsp'

class MytestSpider(CrawlSpider):
    name="che168"
    allowed_domains=["www.che168.com"]
    start_urls=[base_url+str(i)+'exb1x0/' for i in range(1,100)]
    
    def parse(self,response):
        self.log('<===A response from %s just arrived!' % response.url)
        che_list=response.xpath('//*[@filter="0aa0_0a0_0a0_0"]')
        for i in che_list:
            items = Che168Item()
            #self.log(i.xpath('./@dealerid').extract()[0])
            dealerid=i.xpath('./@dealerid').extract()[0]
            infoid=i.xpath('./@infoid').extract()[0]
            detail_url='https://www.che168.com/dealer/%s/%s.html'%(dealerid,infoid)
            self.log('===>url:%s'%detail_url)
            items['dealerid']=dealerid
            items['infoid']=infoid
            yield scrapy.Request(url=detail_url,meta={'items': items},callback=self.parse_article)

    def parse_article(self, response):
        self.log('<===url = %s' % response.url)
        
        items = response.meta['items']
        #++++++++++++网页信息
        items['url'] = response.url
        
        #++++++++++++详细信息
        
        items['car_title'] = response.xpath('//*[@class="car-title"]/h2/text()').extract()[0]
        items['car_price'] = response.xpath('//*[@class="car-price"]/ins/text()').extract()[0]
        items['car_mileage'] = response.xpath('//*[@class="details"]/ul/li[1]/span/text()').extract()[0]
        items['car_firstLicensed'] = response.xpath('//*[@class="details"]/ul/li[2]/span/text()').extract()[0]
        engine_info=response.xpath('//*[@class="details"]/ul/li[3]/span/text()').extract()[0]
        items['car_displacement'] = response.xpath('//*[@class="details"]/ul/li[3]/span/text()').extract()[0]
        items['car_gearbox'] = engine_info.split(u'／')[0]
        items['car_location'] = response.xpath('//*[@class="details"]/ul/li[4]/span/text()').extract()[0]
        items['car_standard'] = response.xpath('//*[@class="details"]/ul/li[5]/span/text()').extract()[0]
        items['car_address'] = response.xpath('//*[@class="car-address"]/text()').extract()[0]
        
        #++++++++++++基本信息
        items['car_inspection_date'] = response.xpath('//div[@id="anchor01"]/ul/li[1]/text()').extract()[0]
        items['car_insurance_date'] = response.xpath('//div[@id="anchor01"]/ul/li[2]/text()').extract()[0]
        items['car_expiration_date'] = response.xpath('//div[@id="anchor01"]/ul/li[3]/text()').extract()[0]
        items['Change_number'] = response.xpath('//div[@id="anchor01"]/ul/li[5]/span[2]/text()').extract()[0]
        items['use'] = response.xpath('//div[@id="anchor01"]/ul/li[6]/text()').extract()[0]
        items['maintain'] = response.xpath('//div[@id="anchor01"]/ul/li[7]/text()').extract()[0]
        items['dealerName'] = response.xpath('//div[@id="anchor01"]/ul/li[8]/text()').extract()[0]
        
        
        
        #++++++++++++车辆配置
        items['car_engine'] = response.xpath('//div[@id="anchor02"]/ul/li[1]/text()').extract()[0]
        items['car_level'] = response.xpath('//div[@id="anchor02"]/ul/li[3]/text()').extract()[0]
        items['car_color'] = response.xpath('//div[@id="anchor02"]/ul/li[4]/text()').extract()[0]
        items['car_fuel_type'] = response.xpath('//div[@id="anchor02"]/ul/li[5]/text()').extract()[0]
        items['car_drive_mode'] = response.xpath('//div[@id="anchor02"]/ul/li[6]/text()').extract()[0]
        
        #++++++++++++车辆图片
        items['car_image']=['http:' + str(i) for i in response.xpath('//img[@name="LazyloadImg"]/@src2').extract()]
        
        yield items