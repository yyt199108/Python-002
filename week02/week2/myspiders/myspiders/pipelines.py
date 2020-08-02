# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

dbInfo = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'test'
}
sql = ['select 1', 'select version()']
result = []


class MyspidersPipeline:

    def __init__(self):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']

    def process_item(self, item, spider):
        title = item['title']
        movieType = item['movieType']
        releaseTime = item['time']
        # output = f'{title},{str(movieType).replace(",", "|")},{str(releaseTime)}\n'
        # print(output)
        # with open('./movie.csv', mode='a+', encoding='utf-8') as f:
        #     f.write(output)
        # return item
        # try:
        # 1 、连接
        connect = pymysql.connect(host=self.host, user=self.user,
                                  password=self.password, database=self.db,
                                  port=self.port, charset='utf8mb4')
        # 2 、创建游标
        cursor = connect.cursor()

        # 3 、执行sql
        sql = "insert into movies values(\"%s\",\"%s\",\"%s\")" % (str(title).replace(",", "|"), str(movieType).replace(",", "|"), str(releaseTime).replace(",", "|"))
        print(sql)
        cursor.execute(sql)
        print(cursor.fetchall())
        connect.commit()
        # 4 、 关闭连接
        cursor.close()
        connect.close()
        # except:
        #     raise Exception
        return item
