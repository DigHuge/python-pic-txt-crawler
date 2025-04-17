# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#爬取数据的item对象
class SkinItem(scrapy.Item):
    name = scrapy.Field() #名字
    date = scrapy.Field() #日期
    time = scrapy.Field() #时长
