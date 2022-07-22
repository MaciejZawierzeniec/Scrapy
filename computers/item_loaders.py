from scrapy.loader import ItemLoader
from itemloaders .processors import MapCompose


def format_price(values):
    return [float(x.replace(' ', '')) for x in values if x != ""]


class PCItemLoader(ItemLoader):
    price_in = MapCompose(str.strip)
    price_out = format_price
    name_in = MapCompose(str.strip)
    cpu_in = MapCompose(str.strip)
    gpu_in = MapCompose(str.strip)
    motherboard_in = MapCompose(str.strip)
