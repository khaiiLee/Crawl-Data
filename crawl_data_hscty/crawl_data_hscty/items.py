# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlDataHsctyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    month_create = scrapy.Field()
    company_name = scrapy.Field()
    company_code = scrapy.Field()
