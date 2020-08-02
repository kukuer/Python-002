import scrapy
from scrapy.selector import Selector
from ..items import Spider2Item


class MaoyanSpider(scrapy.Spider):
    # 爬虫名称
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    # 初始URL列表
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        try:
            for url in self.start_urls:
                yield scrapy.Request(url=url, callback=self.parse)
        except Exception as e:
            print(f'下载异常：{e}')

    def parse(self, response):
        """解析获取排行榜前10名电影信息"""
        selectors = Selector(response=response)\
            .xpath('//div[@class="movie-hover-info"]')

        # 获取电影名称、电影类型、上映时间
        for tags in selectors[:10]:
            item = Spider2Item()
            item['film_name'] = tags.xpath('./div[1]/span/text()')\
                                    .extract_first()
            item['film_type'] = tags.xpath('./div[2]/text()').extract()[1]\
                .strip()
            item['film_time'] = tags.xpath('./div[4]/text()').extract()[1]\
                .strip()
            yield item



