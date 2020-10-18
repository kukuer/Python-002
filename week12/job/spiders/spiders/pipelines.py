# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql


class SpidersPipeline:

    def __init__(self, db_info):
        self.host = db_info['host']
        self.port = db_info['port']
        self.user = db_info['user']
        self.pwd = db_info['password']
        self.db = db_info['db']

        self.con = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.pwd,
            db=self.db
        )

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.get('DB_INFO'))

    def process_item(self, item, spider):

        # sql插入语句
        insert_sql = """
        insert into 
            comment(product_name, comment_con, creat_time)
        values 
            (%s, %s, %s)
        """

        try:
            cursor = self.con.cursor()
            cursor.execute(insert_sql, (
                item['product_name'], item['comment_con'], item['creat_time']))
            cursor.close()
            self.con.commit()
        except Exception as e:
            print(f'异常：{e}')
            self.con.rollback()
        finally:
            self.con.close()

        return item
