#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/7/23
# @Author  : xh.w
# @File    : spider01.py
# 作业1

import requests
import pandas as pd
from bs4 import BeautifulSoup as Bs


def get_film_urls(url, url_path, headers):
    """获取猫眼热门排序页面电影链接"""

    movie_list = []
    response = requests.get(url+url_path, headers=headers)
    # print(f'响应：{response.text}')
    bs_info = Bs(response.text, 'html.parser')
    for tags in bs_info.\
            find_all('div', attrs={'class': 'channel-detail movie-item-title'}):
        for tag in tags.find_all('a',):
            movie_list.append(url + tag.get('href'))

    return movie_list


def get_film_info(movie_url, headers):
    """返回电影信息列表"""

    response = requests.get(movie_url, headers=headers)
    bs_info = Bs(response.text, 'html.parser')
    film_info = bs_info.find('div', attrs={'class': 'movie-brief-container'})
    film_name = film_info.find('h1',).text
    film_type_list = []
    for tag in film_info.find_all('a', ):
        film_type_list.append(tag.text.strip())
    film_type = '/'.join(film_type_list)
    plan_rating = film_info.find_all('li', attrs={'class': 'ellipsis'})[2].text
    return [film_name, film_type, plan_rating]


if __name__ == '__main__':

    url = 'https://maoyan.com'
    url_path = '/films?showType=3'
    headers = {
        'Accept': '*/*;',
        'Connection': 'keep-alive',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Host': 'maoyan.com',
        'Referer': 'http://maoyan.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
    }

    urls = get_film_urls(url, url_path, headers)
    print(urls)

    films_info = []
    for film_url in urls[0:10]:
        print(film_url)
        films_info.append(get_film_info(film_url, headers))
    print(films_info)

    file_name = './test.csv'
    if films_info:
        df_obj = pd.DataFrame(films_info, index=None,
                              columns=['电影名称', '电影类型', '上映日期'])
        df_obj.to_csv(file_name, index=None)
