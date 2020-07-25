# -*- coding: utf-8 -*-
#xpath练习

import requests
import lxml.etree

url = 'https://movie.douban.com/subject/1292052/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
header = {'user-agent': user_agent}

response = requests.get(url, headers=header)

# HTML解析
selector = lxml.etree.HTML(response.text)

# 电影名称
film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print(f'电影名称：{film_name}')

# 上映日期
plan_date = selector.xpath('//*[@id="info"]/span[10]/text()')
print(f'上映日期：{plan_date}')

# 评分
rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
print(f'评分：{rating}')

myList = [film_name, plan_date, rating]

import pandas as pd

movie1 = pd.DataFrame(data=myList)

movie1.to_csv('./movie1.csv', encoding='utf8x', index=False, header=False)