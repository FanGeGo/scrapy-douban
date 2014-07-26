# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class MovieItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    desc = scrapy.Field()
    score = scrapy.Field()

    image_urls = scrapy.Field()
    image_paths = scrapy.Field()
