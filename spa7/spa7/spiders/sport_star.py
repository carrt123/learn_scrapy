import json
import re

import scrapy
from scrapy import Request

from ..items import SportItem


class SportStarSpider(scrapy.Spider):
    name = "sport_star"
    url = "https://spa7.scrape.center/js/main.js"

    def start_requests(self):
        yield Request(url=self.url, callback=self.parse)

    def parse(self, response, **kwargs):
        data = re.search(r'players = \[(.*?)\]', response.text, re.DOTALL).group(1)
        python_friendly_str = data.replace('const', '').replace(';', '').strip() \
            .replace('name:', "'name':") \
            .replace('image:', "'image':") \
            .replace('birthday:', "'birthday':") \
            .replace('height:', "'height':") \
            .replace('weight:', "'weight':")
        # 转换为 Python 字典列表
        players_dict = eval(f"[{python_friendly_str}]")
        for player in players_dict:

            item = SportItem()
            item['name'] = player.get('name')
            item['height'] = player.get('height')
            item['weight'] = player.get('weight')
            item['birthday'] = player.get('birthday')

            yield item
