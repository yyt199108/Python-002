# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MyspidersPipeline:
    def process_item(self, item, spider):
        print('没起作用')
        title = item['title']
        movieType=item['movieType']
        releaseTime=item['time']
        output=f'{title},{str(movieType).replace(",","|")},{str(releaseTime)}\n'
        print(output)
        with open('./movie.csv', mode='a+', encoding='utf-8') as f:
            f.write(output)
        return item
