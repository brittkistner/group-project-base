# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field
import scrapy

class RocketuItem(scrapy.Item):
    baseurl = Field()
    page_url = Field()
    html_content = Field()
    title = Field()
    x_value = Field()
    y_value = Field()

