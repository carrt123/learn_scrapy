import scrapy
from scrapy.http import Request
from ..items import NewsItem


class NewsSpider(scrapy.Spider):
    name = "news"
    limit = 100
    offset = 0
    url = f"https://spa4.scrape.center/api/news/?limit={limit}&offset=%s"
    start_urls = [url % offset]
    def parse(self, response, **kwargs):
        # print(response.text)
        data = response.json()
        for result in data.get('results'):
            item = NewsItem()
            item['title'] = result.get('title')
            item['code'] = result.get('code')
            item['url'] = result.get('url')
            item['website'] = result.get('website')
            item['published_at'] = result.get('published_at')
            item['updated_at'] = result.get('updated_at')
            yield item
        self.offset += self.limit
        if self.offset < 1000:
            yield Request(self.url % self.offset, callback=self.parse)
