    学习爬虫日常记录， 使用scrapy selenium

    所有的爬取数据来自：https://scrape.center/

    推荐一个scrape center 讲解博主, 帮助很大: LLLibra146(zhihu)
    
    创建爬虫项目步骤指令：
    scrapy startproject demo_name
    scrapy genspider spider_name "website"
    scrapy crawl spider_name 
    scrapy crawl spider_name -o "data.json" # 保存爬取数据到json文件中
