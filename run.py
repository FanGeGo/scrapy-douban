# -*- coding: utf-8 -*-
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from douban.spiders.movie import MovieSpider
from scrapy.utils.project import get_project_settings

def setup_crawler(domain):
    spider = MovieSpider()
    settings = get_project_settings()
    crawler = Crawler(settings)
    crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
    crawler.configure()
    crawler.crawl(spider)
    crawler.start()

for domain in ['douban.com', 'douban.com']:
    setup_crawler(domain)

log.start()
reactor.run() # the script will block here until the spider_closed signal was sent
