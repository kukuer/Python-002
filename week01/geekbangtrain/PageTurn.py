# -*- coding: utf-8 -*-
#爬虫翻页练习

import requests
from bs4 import BeautifulSoup as bs

def get_url_name(url):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
    header = {'user-agent': user_agent}

    response = requests.get(url, headers=header)
    bs_info = bs(response.text, 'html.parser')
    for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
        for tag in tags.find_all('a',):
            print(tag.get('href'))
            print(tag.find('span',).text)

# 使用列表推导式生成所有页面tuple
urls = tuple(f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))

for url in urls:
    get_url_name(url)   