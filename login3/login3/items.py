# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    isbn = scrapy.Field()
    name = scrapy.Field()
    authors = scrapy.Field()
    cover = scrapy.Field()
    score = scrapy.Field()
    comments = scrapy.Field()
    publisher = scrapy.Field()
    tags = scrapy.Field()
    price = scrapy.Field()
    introduction = scrapy.Field()
    published_at = scrapy.Field()
    updated_at = scrapy.Field()
    page_num = scrapy.Field()
