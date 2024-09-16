from typing import Iterable

import scrapy
from scrapy import Request
from ..items import MovieItem


class AntiSpider(scrapy.Spider):
    name = "anti"
    base_url = "http://antispider5.scrape.center"

    def start_requests(self):
        for i in range(1, 2):
            yield Request(self.base_url + f"/page/{i}", callback=self.parse)

    def parse(self, response, **kwargs):
        movie_urls = response.css('.name::attr(href)').getall()
        print(response.text)

        for url in movie_urls:
            yield Request(self.base_url + url, callback=self.parse_detail)

    def parse_detail(self, response):
        item = MovieItem()
        item['title'] = response.css('.m-b-sm::text').get()
        item['categories'] = response.css('.categories button span::text').getall()
        info = response.css('.m-v-sm span::text').getall()
        item['region'], item['duration'] = info[0], info[2]
        item['release_date'] = info[3] if len(info) > 3 else None
        item['score'] = response.css('.score ::text').get().strip()
        item['drama'] = response.css('.drama p::text').get().strip()
        yield item
