# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbTopChartItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	title = scrapy.Field()
	directors = scrapy.Field()
	writer = scrapy.Field()
	stars = scrapy.Field()
	popularity = scrapy.Field()
