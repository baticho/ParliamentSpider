# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ParItem(scrapy.Item):
    name = scrapy.Field()
    date = scrapy.Field()
    place = scrapy.Field()
    prof = scrapy.Field()
    lang = scrapy.Field()
    party = scrapy.Field()
    email = scrapy.Field()