import codecs
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

from cars.items import CarsItem

class CarcrawlerSpider(CrawlSpider):
    name = 'CarCrawler'
    allowed_domains = ['autos.mercadolibre.com.ar']
    start_urls = ['http://autos.mercadolibre.com.ar/']
    # start_urls = ['https://autos.mercadolibre.com.ar/hasta-30000-km/capital-federal/_ITEM*CONDITION_2230581_VEHICLE*BODY*TYPE_452759#applied_filter_id%3Dstate%26applied_filter_name%3DUbicación%26applied_filter_order%3D6%26applied_value_id%3DTUxBUENBUGw3M2E1%26applied_value_name%3DCapital+Federal%26applied_value_order%3D6%26applied_value_results%3D761%26is_custom%3Dfalse']
    # start_urls = ['https://autos.mercadolibre.com.ar/hasta-30000-km/capital-federal/2015/_ITEM*CONDITION_2230581_VEHICLE*BODY*TYPE_452759#applied_filter_id%3DVEHICLE_YEAR%26applied_filter_name%3DAño%26applied_filter_order%3D4%26applied_value_id%3D%5B2015-2015%5D%26applied_value_name%3D2015%26applied_value_order%3D7%26applied_value_results%3D9%26is_custom%3Dfalse']
    handle_httpstatus_list = [403]

    rules = (
        Rule(LinkExtractor(allow=()), callback='parsepage', follow=True),
    )

    def parsepage(self, res):
        cars = res.xpath('//li[@class="ui-search-layout__item"]')

        for c in cars:
           car_loader = ItemLoader(item=CarsItem(), selector=c)
           car_loader.default_output_processor = TakeFirst()

           car_loader.add_xpath('title', './/div/div/a/div/div/h2/text()')
           car_loader.add_xpath('brand', './/div/div/a/div/div/h2/text()')
           car_loader.add_xpath('symbol', './/div/div/a/div/div/div/div/span/span/span[@class="price-tag-symbol"]/text()')
           car_loader.add_xpath('price', './/div/div/a/div/div/div/div/span/span/span[@class="price-tag-fraction"]/text()')
           car_loader.add_xpath('model', './/div/div/a/div/div/ul/li[@class="ui-search-card-attributes__attribute"][1]/text()')
           car_loader.add_xpath('kms', './/div/div/a/div/div/ul/li[@class="ui-search-card-attributes__attribute"][2]/text()')
        #    car_loader.add_xpath('imageurl', './/img[@class="thumbnail"]/@src')
           car_loader.add_xpath('carurl', './/div/div/a/@href')

           print('\r\n')
           yield car_loader.load_item()
