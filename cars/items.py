# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose

# def addlink(url):
#     return 'http://autos.mercadolibre.com.ar/' + url.replace('../', '')

class CarsItem(scrapy.Item):
    title = scrapy.Field()
    brand = scrapy.Field()
    symbol = scrapy.Field()
    price = scrapy.Field()
    model = scrapy.Field()
    kms = scrapy.Field()
    # imageurl = scrapy.Field(
    #     input_processor = MapCompose(addlink)
    # )
    carurl = scrapy.Field()
