import base64
import hashlib
import random
import time
import scrapy
from scrapy import Request
from ..items import MovieItem


class MovieSpa2Spider(scrapy.Spider):
    name = "movie_spa2"

    @staticmethod
    def sign(*args):
        t = str(int(time.time()) - random.randint(1, 20))
        data = ",".join(args + (t,))
        # 使用SHA1哈希算法对数据进行哈希
        sha1_hash = hashlib.sha1(data.encode('utf-8')).hexdigest()
        # 将哈希值和时间戳再次连接，并转换为Base64格式
        base64_encoded = base64.b64encode(f"{sha1_hash},{t}".encode('utf-8')).decode('utf-8')
        return base64_encoded

    def start_requests(self):
        for i in range(1, 101):
            s = 'ef34#teuq0btua#(-57w1q5o5--j@98xygimlyfxs*-!i-0-mb'
            detail = base64.b64encode((s + str(i)).encode()).decode()
            token = self.sign("/api/movie/" + detail, '0')
            url = f"https://spa2.scrape.center/api/movie/{detail}/?token={token}"
            yield Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        result = response.json()
        item = MovieItem()
        item['title'] = result.get('name')
        item['categories'] = result.get('categories')
        item['regions'] = result.get('regions')
        item['duration'] = result.get('minute')
        item['release_date'] = result.get('published_at')
        item['score'] = result.get('score')
        item['drama'] = result.get('drama')
        yield item
