#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/8/16
# @Author  : xh.w
# @File    : job.py.py
# 作业要求：请将以下的 SQL 语句翻译成 pandas语句

import pandas as pd

import pymysql


sql = 'SELECT * FROM movies_info'
connect = pymysql.connect(
    host='192.168.3.87',
    port=3306,
    user='root',
    password='123456',
    db='test'
)

# 1. SELECT * FROM data;
df = pd.read_sql(sql, connect)

# 2. SELECT * FROM data LIMIT 10;
df.head(10)
# 3. SELECT id FROM data;  //id 是 data 表的特定一列
df['id']
# 4. SELECT COUNT(id) FROM data;
df['id'].count()
# 5. SELECT * FROM data WHERE id<1000 AND age>30;
df[(df['id'] < 1000) & (df['age'] > 30)]
# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
df.groupby('id')['order_id'].count()
# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
pd.merge(table1, table2, on= 'id', how='inner')
# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
pd.concat([table1, table2])
# 9. DELETE FROM table1 WHERE id=10;
df.drop(11, axis=0)
# 10. ALTER TABLE table1 DROP COLUMN column_name;
df.drop('column_name', axis=1)

