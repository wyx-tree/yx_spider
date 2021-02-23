# Scrapy settings for yaoku_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'yaoku_spider'

SPIDER_MODULES = ['yaoku_spider.spiders']
NEWSPIDER_MODULE = 'yaoku_spider.spiders'

# LOG_LEVEL='ERROR'
