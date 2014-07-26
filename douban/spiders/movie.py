# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from douban.items import MovieItem

tags = ["爱情", "喜剧", "动画", "科幻", "经典", "剧情", "动作", "青春", "悬疑", 
"惊悚", "犯罪", "纪录片", "文艺", "励志", "搞笑", "恐怖", "短片", "战争", "魔幻", 
"黑色幽默", "动画短片", "情色", "传记", "感人", "暴力", "童年", "音乐", "同志", 
"黑帮", "浪漫", "女性", "家庭", "史诗", "童话", "烂片", "cult", ]
one_tag = "爱情"

class MovieSpider(CrawlSpider):
    name = "movie"
    allowed_domains = ["douban.com"]
    start_urls = ["http://movie.douban.com/tag/%s?type=S" % one_tag]
    index = 0
    rules = (
             # 提取匹配 'http://movie.douban.com/tag/爱情' 的翻页
             # Rule(LinkExtractor(allow=(('tag/%s.start=' % quote(one_tag.encode("utf-8"))), ))),
             # 提取匹配 'subject/\d+' 的链接并使用spider的parse_item方法进行分析
             Rule(LinkExtractor(allow=('subject/\d+', )), callback='parse_item'),
             )

    def parse_item(self, response):
        item = MovieItem()
        item['title'] = response.xpath("//div[@id='content']/h1/span[1]/text()").extract()[0]
        item['url'] = response.url
        try:
            item['desc'] = response.xpath("//div[@id='link-report']/span/text()").extract()[0].strip()
        except:
            item['desc'] = '' 
        try:
            item['score'] = response.xpath("//strong[@class='ll rating_num']/text()").extract()[0]
        except:
            item['score'] = 0
        item['image_urls'] = response.xpath("//div[@id='mainpic']/a[@class='nbgnbg']/img/@src").extract()

        print item['title'], item['score'],item['url'],item['desc']
        yield item
