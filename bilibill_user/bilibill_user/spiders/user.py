import scrapy


class UserSpider(scrapy.Spider):
    name = "user"
    allowed_domains = ["bilibill"]
    start_urls = ["https://bilibill"]

    def parse(self, response):
        pass
