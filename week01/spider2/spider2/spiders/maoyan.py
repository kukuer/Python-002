import scrapy
from scrapy.selector import Selector
from ..items import Spider2Item


class MaoyanSpider(scrapy.Spider):
    # 爬虫名称
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    # 初始URL列表
    start_urls = ['https://maoyan.com/films?showType=3']
    # 猫眼首页
    url = 'https://maoyan.com'

    def parse(self, response):
        """解析获取排行榜前10名电影链接地址，并请求"""
        selectors = Selector(response=response)\
            .xpath('//div[@class="channel-detail movie-item-title"]/a/@href')
        for url_path in selectors.extract()[0:10]:
            yield scrapy.Request(url=self.url+url_path, callback=self.parse2)

    def parse2(self, response):
        film = Selector(response=response)\
            .xpath('//div[@class="movie-brief-container"]')
        item = Spider2Item()
        item['film_name'] = film.xpath('./h1/text()').extract_first()
        item['film_type'] = '/'\
            .join([i.strip() for i in film.xpath('./ul/li/a/text()').extract()])
        item['film_time'] = film\
            .xpath('//div[@class="movie-brief-container"]/ul/li[3]/text()')\
            .extract_first()
        yield item


