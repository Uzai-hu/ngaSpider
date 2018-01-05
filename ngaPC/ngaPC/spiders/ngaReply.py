# -*- coding: utf-8 -*-
import scrapy
from ngaPC.items import NgapcItem

class NgareplySpider(scrapy.Spider):
    name = 'ngaReply'
    allowed_domains = ['nga.178,com']
    start_urls = ['http://nga.178.com/thread.php?&authorid=42437889&searchpost=1&page=1']

    temp_url = start_urls

    def parse(self, response):
        node_list = response.xpath("//table[@id='topicrows']/tbody")

        next_Url = response.xpath("//a[@class='pager_spacer']")

        print ("==============")
        print response.body
        print next_Url
        print ("==============+++++")

        # items = []
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




        pass
