# Scrapy settings for par project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'par'

SPIDER_MODULES = ['par.spiders']
NEWSPIDER_MODULE = 'par.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'INFO'
DOWNLOAD_DELAY = 15

ITEM_PIPELINES = {
    'par.pipelines.ParPipeline': 100,
    
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'login (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

FEEDS = {
    './files/items.jl': {
        'format': 'jsonlines',
        'encoding': 'utf8',
        'store_empty': False,
        'item_export_kwargs': {
           'export_empty_fields': True,
        },
    },
}

DOWNLOADER_MIDDLEWARES = {
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

'''ROTATING_PROXY_LIST = [
    '163.172.47.182:3128',
    '51.81.113.246:80',
]

ROTATING_PROXY_PAGE_RETRY_TIMES = 2'''
