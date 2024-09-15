import scrapy
from ..items import BookItem
from scrapy import Request


class BooksSpider(scrapy.Spider):
    name = "books"
    limit = 50
    page_url = f"https://spa5.scrape.center/api/book/?limit={limit}&offset=%s"
    book_url = "https://spa5.scrape.center/api/book/%s"
    offset = 0

    def start_requests(self):
        yield Request(self.page_url % self.offset, callback=self.parse)

    def parse(self, response, **kwargs):
        data = response.json()
        for result in data['results']:
            yield Request(self.book_url % result['id'], callback=self.parse_book)

        self.offset += self.limit
        if self.offset <= 1000:
            yield Request(self.page_url % self.offset, callback=self.parse)

    def parse_book(self, response):
        # 解析书籍详情页
        data = response.json()
        item = BookItem()
        item['isbn'] = data['isbn']
        item['name'] = data['name']
        item['price'] = data['price']
        item['authors'] = '/'.join([author.strip() for author in data['authors']])
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
