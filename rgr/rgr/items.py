# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RgrItem(scrapy.Item):
    logo = scrapy.Field()
    telefone = scrapy.Field()
    website = scrapy.Field()
