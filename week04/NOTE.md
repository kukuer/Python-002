# 学习笔记

## pandas简介

### sklearn模块

```python
from sklearn import datasets # 引数据集

# 鸢尾花数据集
iris = datasets.load_iris()
x, y = iris.data, iris.target
# 查看特征
iris.feature_names
# 查看标签
iris.target_names
```

load_xxx加载数据

load_boston  Boston房价

load_digits 手写体

### pandas

 **2. pandas 中文文档：**
https://www.pypandas.cn/
sklearn-pandas
**3. 安装参考文档：**
https://pypi.org/project/sklearn-pandas/1.5.0/
**4. Numpy 学习文档：**
https://numpy.org/doc/
**5. matplotlib 学习文档：**
https://matplotlib.org/contents.html 

## pandas基本数据类型

**Series**

类似一维数组

1. 通过list/dict构建Series

   series_obj =  pandas.Series(list)

   ```
   >>> s1 = pd.Series({'a':11, 'b':22, 'c':33})
   >>> s2 = pd.Series([11, 22, 33], index = ['a', 'b', 'c'])
   >>> s1
   a    11
   b    22
   c    33
   dtype: int64
   >>> s2
   a    11
   b    22
   c    33
   dtype: int64
   ```

   

2. 由数据和索引组成：索引在左，数据在右，索引都是自动创建

   | index | element |
   | :---: | :-----: |
   |   0   |    1    |
   |   1   |    2    |
   |   2   |    3    |

3. 获取索引/数据

   series_obj.index、series_obj.values

4. 预览数据：

   series_obj.head(n)

5. 通过索引获取数据
   series_obj[index]

6. name

   series_obj.name, series_obj.index.name

**DataFrame**

- 表格数据类型，类似二维或者高维数组
- 每列数据可以是不同的类型
- 索引：行索引（index），列索引（columns）

1. 通过dict构建

## 数据导入

```
import pandas as pd


pd.read_excel(r'data.xlsx')
pd.read_csv(r'data.csv')
pd.read_sql(sql, connect)
```

