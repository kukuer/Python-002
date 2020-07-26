# 学习笔记

## url下载：

下载模块：

1. 第三方库：requests

   ```python
   response = requests.get(url, headers=[http头])
   # 状态码
   response.status_code
   # 响应内容
   response.text
   ```

2. 标准库：uillib2

   ```python
   reqesut = urllib2.Request(url=url, headers=[http头])
   response = urllib2.urlopen(request)
   response.getcode()
   response.reade.decode()
   ```

## 网页解析

### bs4：

创建对象：

```python
bs_obj = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
```

- 按类型提取所有节点

```python
# 提取所有链接,返回链接列表
link_list = bs_obj.find_all('a') 
for link in link_list:
    # 节点标签名称
    print(link.name)
    # 获取节点href属性
    print(link['href'])
    # 获取节点文字
    print(link.get_text())
```

- 按属性查找节点

  ```python
  # 根据属性提取一条链接
  link = bs_obj.find('a', attrs={'id': 'link2'})
  print link.name, link['href'], link.get_text()
  ```

### Xpath：

| 表达式   | 描述                     |
| -------- | :----------------------- |
| 节点名称 | 获取次节点所有子节点。   |
| /        | 从根节点获取，包含根节点 |
| //       | 从满足条件的             |
| .        | 当前节点                 |
| ..       | 当前节点的父节点         |
| @        | 根据属性获取             |
|          |                          |

## Scrapy:

### 创建Spider

  1. 创建工程：scrapy startproject project_name

  2. 生成Spider: scrapy genspider spider_name url

     Scrapy工程可以有多个Spider

3. 运行Spider： scrapy crawl spider_name

### 编写Spider步骤

		1. 定义Item： scrapy.Field()
	
		2. 编写Spider:  编写爬虫逻辑，给自定义Item赋值
	
	 - 默认使用start_urls作为初始url生成Request，默认将parse作为回到方法
	
	   在parse中解析start_url响应。
	
	 - 如果不使用默认，可以通过实现start_requests，初始实现自定义方法
	
	 - scrapy.Request，通过回调callback参数指向解析方法
	
		3. pipelines:  保存数据，return item

### Scrapy命令：

help: 查看帮助，scrapy --help

list: 查看Scrapy工程下spider，scrapy list





