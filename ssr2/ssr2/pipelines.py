# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class Ssr2Pipeline:
    def open_spider(self, spider):
        # 打开一个文件用于写入，并确保文件在开始时是空的
        self.file = open('movies.json', 'w', encoding='utf-8')
        # 写入JSON数组的开头
        self.file.write('[')

    def close_spider(self, spider):
        # 在文件末尾添加JSON数组的结束符号，并关闭文件
        self.file.write('\n]')
        self.file.close()

    def process_item(self, item, spider):
        # 将项目转换为字典
        item_dict = ItemAdapter(item).asdict()
        # 将字典转换为JSON格式的字符串
        json_line = json.dumps(item_dict, ensure_ascii=False)
        # 检查是否是第一个项目，如果不是则在前面添加逗号
        if self.file.tell() > 1:
            json_line = ',\n' + json_line
        # 将JSON字符串写入文件
        self.file.write(json_line)
        return item
