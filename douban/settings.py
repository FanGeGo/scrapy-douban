# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_douban project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os
DOUBAN_PATH = os.path.dirname(os.path.abspath(__file__))

BOT_NAME = 'scrapy_douban'

SPIDER_MODULES = ['douban.spiders']
NEWSPIDER_MODULE = 'douban.spiders'
ITEM_PIPELINES = {
    'douban.pipelines.ImagesPipeline': 50,
    'douban.pipelines.DuplicatesPipeline': 100,
    'douban.pipelines.MoviePipeline': 200,
}
IMAGES_STORE = os.path.join(DOUBAN_PATH, 'images')

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'

# use proxy
# Retry many times since proxies often fail
RETRY_TIMES = 10
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 90,
        'douban.randomproxy.RandomProxy': 100,
        'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
}

# Proxy list containing entries like
# http://host1:port
# http://username:password@host2:port
# http://host3:port
# ...
PROXY_LIST = os.path.join(DOUBAN_PATH, 'proxy_list.txt')
