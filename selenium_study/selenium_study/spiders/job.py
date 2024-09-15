import scrapy
from scrapy import Request
from ..items import SeleniumStudyItem


class JobSpider(scrapy.Spider):
    name = "job"
    url = "https://job.bytedance.com/society/position?current=%s"
    offset = 1

    def start_requests(self):
        yield Request(self.url % self.offset, callback=self.parse)

    def parse(self, response, **kwargs):

        node_list = response.xpath('//div[@class="positionItem__1giWi positionItem"]')
        for node in node_list:
            item = SeleniumStudyItem()
            item['PositionName'] = node.xpath('.//span[@class="positionItem-title-text"]//text()').extract()
            item['WorkLocation'] = node.xpath(
                './/div[@class="subTitle__3sRa3 positionItem-subTitle"]//text()[1]').extract()
            item['PositionType'] = node.xpath(
                './/div[@class="subTitle__3sRa3 positionItem-subTitle"]//text()[2]').extract()
            item['PositionInfo'] = node.xpath(
                'normalize-space(.//div[@class="jobDesc__3ZDgU positionItem-jobDesc"]//text())').extract()
            yield item

        self.offset += 1
        if self.offset <= 10:
            yield Request(self.url % self.offset, callback=self.parse)

