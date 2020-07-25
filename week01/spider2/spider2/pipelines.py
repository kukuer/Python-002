# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


class Spider2Pipeline:

    def process_item(self, item, spider):
        film_name = item['film_name']
        film_type = item['film_type']
        film_time = item['film_time']
        output = f'{film_name},\t{film_type},\t{film_time},\n'
        with open('./filmInfo.csv', mode='a+', encoding='utf-8') as f:
            f.write(output)
        return item
