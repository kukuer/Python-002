from datetime import datetime

import scrapy
from scrapy.selector import Selector
from spiders.items import ShampoosItem

class ShampoosSpider(scrapy.Spider):
    name = 'shampoos'
    allowed_domains = ['www.smzdm.com']
    # start_urls = ['https://www.smzdm.com/fenlei/xifahufa/h5c4s0f0t0p1/#feed-main/']
    start_urls = ['https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        '''
        爬取前10产品链接
        '''
        item = ShampoosItem()
        item['creat_time'] = datetime.now().strftime('%Y-%m-%d')
        selectors = Selector(response=response).xpath('//h5[@class="feed-block-title"]')
        for tags in selectors[:10]:
            product_name = tags.xpath('./a/text()').extract_first()
            print(f'-------- {product_name} -----------')
            url = tags.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=url, meta={'product_name': product_name, 'item': item}, callback=self.get_comment_page)

    def get_comment_page(self,response):
        """
        获取评论分页链接
        """
        product_name = response.meta['product_name']
        print(f'========= 开始爬取：{product_name} ===============')
        item = response.meta['item']
        pagination = Selector(response=response)\
            .xpath('//div[@id="comment"]/div[1]/ul[@class="pagination"]/li/a/@href')\
            .extract()
        comment_num = Selector(response=response).xpath('//em[@class="commentNum"]')

        # 无评论产品
        if comment_num == 0:
            item['product_name'] = product_name
            item['comment_con'] = None
            yield item

        # 有评论无分页
        if not pagination:
            selectors = Selector(response=response).xpath('//div[@id="commentTabBlockNew"]/ul/li/div[2]/div[2]/div[1]')
            print(f'selector: {selectors}')
            for tags in selectors:
                comment_con = tags.xpath('./p/span/text()').extract_first()
                item['product_name'] = product_name
                item['comment_con'] = comment_con
                yield item

        # 评论分页
        for page in pagination[:-2]:
            yield scrapy.Request(url=page, meta={'item': item, 'product_name': product_name}, callback=self.get_comment_con, dont_filter=True)

    def get_comment_con(self, response):
        """
        爬取所有评论信息
        """
        product_name = response.meta['product_name']
        item = response.meta['item']
        selectors = Selector(response=response).xpath('//div[@class="comment_con"]')
        for tags in selectors:
            comment_con = tags.xpath('./p/span/text()').extract_first()
            item['product_name'] = product_name
            item['comment_con'] = comment_con
            yield item


