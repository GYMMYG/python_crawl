import scrapy
import time
import urllib.request
from quotetutorial.items import QuoteItem
from quotetutorial.items import AuthorItem
from protego import Protego


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')

        for quote in quotes:
            # change piplines to get two csv
            # first csv
            item = QuoteItem()
            text = quote.css('.text::text').extract_first()
            author = quote.css('.author::text').extract_first()
            tags = quote.css('.tags .tag::text').extract()
            item['text'] = text
            item['author'] = author
            item['tags'] = ','.join(tags)
            yield item

            #second csv
            #into about page
            about = quote.css('a::attr(href)').extract_first()
            about_url = response.urljoin(about)
            yield scrapy.Request(url = about_url, callback=self.parse_author)
        #next page
        next = response.css('.pager .next a::attr(href)').extract_first()
        next_url = response.urljoin(next)
        yield scrapy.Request(url=next_url, callback=self.parse)

    def parse_author(self, response):
        for sel in response.css('html').extract():
            item = AuthorItem()
            author_details = response.css('.container .author-details')

            item['author_title'] = author_details.css('.author-title::text').extract_first()

            #split dates to data and year
            born_dates = author_details.css('.author-born-date::text').extract_first()
            item['born_date'],item['born_year'] = born_dates.split(',')

            '''
            remove ‘in’ in location
            split it to city and country 
            ！！！sometimes there is no city ,put unknow
            '''
            born_location = author_details.css('.author-born-location::text').extract_first()
            born_location = born_location.replace('in ','')
            item['born_country'] = born_location.split(',')[-1]
            if len(born_location.split(',')) > 1:
                item['born_city'] = born_location.split(',')[0]
            else:
                item['born_city'] = None

            item['description'] = author_details.css('.author-description::text').extract_first()
            yield item


