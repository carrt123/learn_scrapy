# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SeleniumStudyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    PositionName = scrapy.Field()
    WorkLocation = scrapy.Field()
    PositionType = scrapy.Field()
    PositionInfo = scrapy.Field()

