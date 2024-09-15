import scrapy
from scrapy import Request
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ..items import MovieItem


class AntiSpider(scrapy.Spider):
    name = "antispider"
    url = "https://antispider1.scrape.center/detail/%s"

    def start_requests(self):
        for i in range(1, 101):
            yield Request(self.url % i, callback=self.parse_detail)

    def parse_detail(self, response):
        item = MovieItem()
        item['title'] = response.css('.m-b-sm::text').get()
        categories = response.css('.categories button span::text').getall()
        item['categories'] = [category.strip() for category in categories]
        info = response.css('.m-v-sm span::text').getall()
        item['region'], item['duration'] = info[0], info[2]
        item['release_date'] = info[3] if len(info) > 3 else None
        item['score'] = response.css('.score ::text').get().strip()
        item['drama'] = response.css('.drama p::text').get().strip()
        yield item
