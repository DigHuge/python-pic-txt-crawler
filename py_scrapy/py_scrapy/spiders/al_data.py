import scrapy
from scrapy import Selector,Request
from scrapy.http import HtmlResponse

from py_scrapy.items import SkinItem


class AlDataSpider(scrapy.Spider):
    name = "al_data"
    allowed_domains = ["movie.douban.com"]
    #start_urls = ["https://wiki.biligame.com/blhx/%E6%8D%A2%E8%A3%85%E5%9B%BE%E9%89%B4"] #换装图鉴

    def start_requests(self): #直接构造url给引擎
        for i in range(10):
            yield Request(url=f'?start={i*25}&filter=')

    def parse(self, response:HtmlResponse,**kwargs):
        sel = Selector(response)
        list_items = sel.css('#content > div > div.article > ol > li') #选择器对象
        for list_item in list_items:
            detail_url = list_item.css('div.info > div.hd > a:attr(href)').extract_first() #拿详情页信息的url
            skin_item = SkinItem()
            # skin_item["name"] = list_item.css("a:nth-child(1)::text").extract_first() #名字 拿a标签下的文本
            # skin_item["date"] = list_item.css("td:nth-child(12)::text").extract_first() #日期，待完善
            skin_item["name"] = list_item.css("span.title::text").extract_first()
            skin_item["date"] = list_item.css("span.rating_num::text").extract_first()
            yield Request(url=detail_url, #重新产生个请求 去爬新页面的详情信息，调用parse_detail方法爬取
                          callback=self.parse_detail,
                          cb_kwargs={'item':skin_item}) #传item项，待爬取到数据后再度组装
            #yield skin_item

    def parse_detail(self,response:HtmlResponse,**kwargs): #拿时长
        skin_item = kwargs['item'] #获取传来的数组，用来组装
        sel = Selector(response)
        sel.css('span[property="v:runtime"]:attr(content)').extract_first() #拿时长
        skin_item["time"] = ''
        yield skin_item

        # hrefs_list  = sel.css('div.paginator > a::attr(href)') #拿herf标签的属性，即url
        # for href in hrefs_list:
        #     url = response.urljoin(href.extract())
        #     yield Request(url=url)


