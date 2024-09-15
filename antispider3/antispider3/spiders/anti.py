import scrapy
from scrapy import Request
from ..items import BookItem
import re

class AntiSpider(scrapy.Spider):
    name = "anti"
    page = 1
    page_url = "https://antispider3.scrape.center/page/%s"

    def start_requests(self):
        yield Request(url=self.page_url % self.page, callback=self.parse)

    def parse(self, response, **kwargs):
        items = response.css('.el-card__body')
        print('********',len(items))
        for item in items:
            book = BookItem()
            chars = {}
            spans = item.css('.name > span')
            if spans:  # 如果有找到span元素
                for b in spans:
                    style_value = b.attrib.get('style', '')
                    match = re.search(r'left:\s*(\d+)', style_value)
                    if match:
                        position = int(match.group(1))  # 提取left值
                        char_text = b.xpath('.//text()').get().strip()
                        chars[position] = char_text
                sorted_chars = [chars[pos] for pos in sorted(chars.keys())]
                book['name'] = ''.join(sorted_chars)
            else:
                book['name'] = item.css('.name::text').get()
            yield book

        self.page += 1
        if self.page <= 20:
            yield Request(url=self.page_url % self.page, callback=self.parse)
