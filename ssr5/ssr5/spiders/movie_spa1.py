import scrapy
from ..items import MovieItem

class MovieSpa1Spider(scrapy.Spider):
    name = "movie_spa1"
    allowed_domains = ["spa1.scrape.center"]
    start_urls = [f"https://spa1.scrape.center/api/movie/{i}" for i in range(1, 41)]

    def parse(self, response, **kwargs):
        item = MovieItem()
        result = response.json()
        item['title'] = result['name']
        item['categories'] = result['categories']
        item['region'], item['duration'] = result['regions'], result['minute']
        item['release_date'] = result['published_at']
        item['score'] = result['score']
        item['drama'] = result['drama']
        yield item
