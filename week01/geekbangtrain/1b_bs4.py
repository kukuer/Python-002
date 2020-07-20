# -*- coding: utf-8 -*-
#使用bs4解析网页

import requests
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
header = {'user-agent': user_agent}
top250_url = 'https://movie.douban.com/top250'

response = requests.get(top250_url, headers=header)
bs_info = bs(response.text, 'html.parser')
for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
    for tag in tags.find_all('a',):
        print(tag.get('href'))
        print(tag.find('span',).text)
