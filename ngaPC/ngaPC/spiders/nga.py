# -*- coding: utf-8 -*-
import scrapy
from ngaPC.items import NgapcItem

#补URL爬虫

class NgaSpider(scrapy.Spider):
    name = 'nga'
    allowed_domains = ['nga.178.com']
    baseUrl = "http://nga.178.com/thread.php?&authorid=42437889&searchpost=1&page="
    offset = 1
    start_urls = [baseUrl+str(offset)]


    def parse(self, response):
        node_list = response.xpath("//table[@id='topicrows']/tbody")

        for node in node_list:

            item = NgapcItem()


            reply = node.xpath("./tr/td[@class='c2']//span/text()").extract()
            topicTitle = node.xpath(".//a[@class='topic']/text()").extract()
            topicArrdess = node.xpath(".//a[@class='topic']/@href").extract()
            topicClass = node.xpath(".//span[@class='titleadd2']/a/text()").extract()


            if not len(topicTitle) or not len(topicClass) or not len(reply):
                continue

            item["topicTitle"] = topicTitle[0].encode("utf-8")
            item["topicArrdess"] = topicArrdess[0].encode("utf-8")
            item["topicClass"] =  topicClass[0].encode("utf-8")
            item["reply"] = reply[len(reply)-1].encode("utf-8")

            yield item

        if len(node_list) != 0:
            self.offset += 1
            url = self.baseUrl + str(self.offset)
            yield scrapy.Request(url,callback=self.parse)
