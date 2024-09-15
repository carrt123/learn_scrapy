# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Ssr1Pipeline:
    def open_spider(self, spider):
        self.file = open('ssr1.json', 'w', encoding='utf-8')
        self.file.write('[\n')

    def close_spider(self, spider):
        self.file.write('\n]')
        self.file.close()

    def process_item(self, item, spider):

        line = json.dumps(dict(item), ensure_ascii=False, indent=4) + ',\n'
        self.file.write(line)
        return item
