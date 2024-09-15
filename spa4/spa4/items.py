# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    website = scrapy.Field()
    published_at = scrapy.Field()
    updated_at = scrapy.Field()

