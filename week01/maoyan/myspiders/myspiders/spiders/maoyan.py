# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from myspiders.items import MyspidersItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    # 自定义入口
    def start_requests(self):
        # for i in range(0, 9):
        i = 0
        url = f'https://maoyan.com/films?showType=3&offset={i * 30}'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    # 使用Scrapy框架和XPath抓取猫眼电影
    # 的前10个电影名称、电影类型和上映时间，
    # 并以UTF - 8字符集保存到csv格式的文件中。
    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
        for movie in movies:
            item = MyspidersItem()
            # print(movie)
            title = movie.xpath('./a/text()').extract()[0]
            link = f'https://maoyan.com{movie.xpath("./a/@href").extract()[0]}'
            print(title, link)
            item['title'] = title
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2, dont_filter=True)

    def parse2(self, response):
        item = response.meta['item']
        movie2 = Selector(response=response)
        # movieTypes=movie2.xpath('//li[@class="ellipsis"]')
        # 电影类型
        movieTypes = movie2.xpath('//li[@class="ellipsis"][1]//a/text()').extract()
        print(movieTypes)
        # 上映时间
        movieReleaseTime = movie2.xpath('//li[@class="ellipsis"][3]/text()').extract()
        print(movieReleaseTime)
        item['movieType'] = str(movieTypes)
        item['time'] = movieReleaseTime
        yield item