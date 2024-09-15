import scrapy
from ..items import MovieItem
from scrapy import Request

class MovieSsr2Spider(scrapy.Spider):
    name = "movie_ssr2"
    allowed_domains = ["ssr2.scrape.center"]
    start_urls = ["http://ssr2.scrape.center/"]
    base_url = "http://ssr2.scrape.center"

    def parse(self, response):
        movie_urls = response.css('.name::attr(href)').getall()

        for url in movie_urls:
            yield Request(self.base_url + url, callback=self.parse_detail)

        # 翻页
        next_page = response.css('.next::attr(href)').get()
        if next_page is not None:
            yield Request(response.urljoin(next_page), callback=self.parse)

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
