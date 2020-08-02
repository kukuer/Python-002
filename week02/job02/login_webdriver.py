#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/8/2
# @Author  : Ropon
# @File    : login_webdriver.py

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


index_url = 'https://shimo.im'

try:
    driver = webdriver.Chrome()
    # 打开石墨文档首页
    driver.get(index_url)
    # 显示等待，判断是否进入首页
    WebDriverWait(driver, 5).until(EC.title_contains('石墨文档'))
    # 点击进入登录页面
    login_button = driver.find_element_by_xpath("//div[@class='entries']/a[2]")
    login_button.click()
    
    # 登录
    driver.find_element_by_xpath("//input[@name='mobileOrEmail']")\
        .send_keys('17791619640')
    driver.find_element_by_xpath("//input[@name='password']")\
        .send_keys('123456')
    driver.find_element_by_xpath(
        "//button[@class='sm-button submit sc-1n784rm-0 bcuuIb']").click()
    
except Exception as e:
    print(e)
finally:
    driver.close()
