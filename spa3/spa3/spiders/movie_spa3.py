from typing import Iterable

import scrapy
from scrapy import Request
from ..items import MovieItem


class MovieSpa3Spider(scrapy.Spider):
    name = "movie_spa3"
    offset = 0
    url = "https://spa3.scrape.center/api/movie/?limit=10&offset=%s"

    def start_requests(self):

        yield Request(self.url % self.offset, callback=self.parse)

    def parse(self, response, **kwargs):
        data = response.json()

        for result in data["results"]:
            item = MovieItem()
            item['title'] = result.get('name')
            item['categories'] = result.get('categories')
            item['regions'] = result.get('regions')
            item['duration'] = result.get('minute')
            item['release_date'] = result.get('published_at')
            item['score'] = result.get('score')
            item['drama'] = result.get('drama')
            yield item
        self.offset += 10
        if self.offset < data['count']:

            yield Request(self.url % str(int(self.offset) + 10), callback=self.parse)



