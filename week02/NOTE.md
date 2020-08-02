# 学习笔记

## 1. 异常捕获

```python
try:
    pass
except Exception as e:
    print(e)
else:
    pass
finally:
    pass
```

先执行try下代码，发生异常时执行except下代码，没有异常执行else代码，

无论是否发生异常都要执行finally下代码。

## 2. 使用PyMySQL操作数据库

```python
import pymysql

# 创建数据库连接
connect = pymysql.connect(host, port, user, password, db)
# 获取游标，开始一个事务
cursor = connect.cursor()
# 执行sql
cursor.execute(sql语句)
# 执行完成后，关闭游标
cursor.close()
# 提交事务
connect.commit()
# 如果事务失败，可以回滚事务
connect.rollback()
# 数据库操作完成后，关闭连接
connect.close()
```

## 3. Webdriver

```python
# 安装selenium
pip install selenium
# 下载浏览器驱动，设置环境变量
chrome驱动：https://chromedriver.storage.googleapis.com/index.html
    
from selenium import webdriver
# 启动浏览器
dirvier = webdriver.Chrome()
# 打开页面
driver.get(url)
# 通过xpath获取页面元素
driver.find_element_by_xpath(元素xpath路径)
```

