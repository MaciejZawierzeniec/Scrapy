import scrapy
from scrapy import Field


class PCItem(scrapy.Item):
    name = Field()
    price = Field()
    cpu = Field()
    gpu = Field()
    motherboard = Field()
