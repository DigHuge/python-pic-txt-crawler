# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 处理数据的“管道”
# hook（钩子）方法，框架自己调动
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl
import pymysql

# class Db_PyScrapyPipeline: #写入数据库，注意要去setting文件修改配置
#     def __init__(self):
#         self.conn = pymysql.connect(host='',port=3306,user='',password='',database='',charset='utf-8')
#         self.cursor = self.conn.cursor()
#         self.data = [] #搞个容器，存一些再一起写入
#
#     def close_spider(self,spider):
#         if len(self.data)>0:
#             self._write_to_db()
#         self.conn.close()
#
#     def process_item(self, item, spider):
#         name = item.get('name', '')
#         rank = item.get('date', '')
#         # self.cursor.execute('insert into tb_top_movie(title,rank) values (%s %s)',(name,rank))
#         self.data.append((name,rank))
#         if len(self.data) == 100:
#             self._write_to_db()
#             self.data.clear()
#         return item
#
#     def _write_to_db(self): #写到数据库中
#         self.cursor.executemany('insert into tb_top_movie(title,rank) values (%s %s)',
#                             self.data)
#         self.conn.commit()

class PyScrapyPipeline:

    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.w_sheet = self.wb.active
        self.w_sheet.title = 'top250'
        self.w_sheet.append(('名字','评分','时长'))#标头名字

    def close_spider(self,spider): #爬虫关闭时执行
        self.wb.save('movie_data.xlsx')

    def process_item(self, item, spider): #拿到一次数据就执行一次
        name = item.get('name','')
        rank = item.get('date','')
        self.w_sheet.append((name,rank))
        return item
