
# -*- coding: utf-8 -*-
 
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
 
import scrapy
 
 
class QuoteItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    born_date = scrapy.Field()
    born_year = scrapy.Field()
    born_country = scrapy.Field()
    born_city = scrapy.Field()
    description = scrapy.Field()


#
# class AuthorItem(scrapy.Item):
#     author_title = scrapy.Field()
#     born_date = scrapy.Field()
#     born_year = scrapy.Field()
#     born_country = scrapy.Field()
#     born_city = scrapy.Field()
#     description = scrapy.Field()