from abc import ABC

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider

from ..item_loaders import PCItemLoader
from ..items import PCItem

NO_PAGES = 22


class PCSpider(CrawlSpider, ABC):
    name = 'pc_spider'
    allowed_domains = ['komputronik.pl']
    start_urls = ['https://www.komputronik.pl/search-filter/5801/komputery-do-gier?p=' + str(x) for x in range(1, NO_PAGES)]
    custom_settings = {
        'ITEM_PIPELINES': {'computers.pipelines.ComputersPipeline': 300}
    }
    rules = (
        Rule(LinkExtractor(allow='product'), callback='parse_details'),
    )

    def parse_details(self, response):
        loader = PCItemLoader(PCItem(), response=response)
        loader.add_xpath('name', '//*[@id="p-inner-name"]/h1/text()')
        loader.add_xpath('price', '//*[@id="p-inner-prices"]/div[1]/span/span/text()')
        loader.add_xpath('cpu', '//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[3]/td/text()')
        loader.add_xpath('gpu', '//*[@id="p-content-specification"]/div[2]/div/div[3]/table/tbody/tr[2]/td/a/text()')
        loader.add_xpath('motherboard', '//*[@id="p-content-specification"]/div[2]/div/div[7]/table/tbody/tr[1]/td/text()')

        yield loader.load_item()
