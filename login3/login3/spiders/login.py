from typing import Iterable

import scrapy
from scrapy import Request
from ..items import BookItem


class LoginSpider(scrapy.Spider):
    name = "login"
    limit = 100
    offset = 0
    pape_url = f"https://login3.scrape.center/api/book/?limit={limit}&offset=%s"
    book_url = "https://login3.scrape.center/api/book/%s"
    jwt = ""

    def start_requests(self):
        yield scrapy.FormRequest(url='https://login3.scrape.center/api/login', formdata={
            'username': 'admin', 'password': 'admin'}, callback=self.parse)

    def parse(self, response, **kwargs):
        result = response.json()
        if 'token' in result:
            self.jwt = result['token']
        yield Request(url=self.pape_url % self.offset, callback=self.parse_page)

    def parse_page(self, response):
        result = response.json()
        for item in result.get('results'):
            yield Request(url=self.book_url % item['id'], callback=self.parse_detail)

        self.offset += self.limit
        if self.offset <= result['count']:
            yield Request(url=self.pape_url % self.offset, callback=self.parse_page)

    def parse_detail(self, response):
        data = response.json()
        item = BookItem()
        item['isbn'] = data['isbn']
        item['name'] = data['name']
        item['price'] = data['price']
        item['authors'] = [author.strip() for author in data['authors']]
        item['score'] = data['score']
        item['cover'] = data['cover']
        item['comments'] = data['comments']
        item['publisher'] = data['publisher']
        item['tags'] = data['tags']
        item['introduction'] = data['introduction']
        item['published_at'] = data['published_at']
        item['updated_at'] = data['updated_at']
        item['page_num'] = data['page_number']
        yield item
