import scrapy
from scrapy import Request
from ..items import MovieItem


class LoginSpider(scrapy.Spider):
    name = "login"
    base_url = "https://login2.scrape.center"
    cur_page = 1

    def start_requests(self):
        yield scrapy.FormRequest(self.base_url + '/login', formdata={"username": "admin", "password": "admin"},
                                 callback=self.parse)

    def parse(self, response, **kwargs):
        movie_urls = response.css('.name::attr(href)').getall()
        print(movie_urls)

        for url in movie_urls:
            yield Request(self.base_url + url, callback=self.parse_detail)

        # 翻页
        self.cur_page += 1
        if self.cur_page <= 10:
            yield Request(response.urljoin(f'/page/{self.cur_page}'), callback=self.parse)

    def parse_detail(self, response):
        item = MovieItem()
        item['title'] = response.css('.m-b-sm::text').get()
        item['categories'] = response.css('.categories button span::text').getall()
        info = response.css('.m-v-sm span::text').getall()
        item['regions'], item['duration'] = info[0], info[2]
        item['release_date'] = info[3] if len(info) > 3 else None
        item['score'] = response.css('.score ::text').get().strip()
        item['drama'] = response.css('.drama p::text').get().strip()
        yield item
