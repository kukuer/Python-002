# -*- coding: utf-8 -*-

import pymysql
from sqlalchemy import create_engine
import pandas as pd
from snownlp import SnowNLP


sql = """
select
    product_name, comment_con, creat_time
from
    comment
"""

con = create_engine('mysql+pymysql://root:123456@192.168.3.87:3306/my_spider?charset=utf8')

df = pd.read_sql(sql, con)

def _sentiment(text):
    s = SnowNLP(text)
    return s.sentiments

df["sentiment"] = df.comment_con.apply(_sentiment)

df.to_sql(name="sentiment",con=con, if_exists='append', index=False)

