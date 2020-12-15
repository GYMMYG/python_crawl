import scrapy
import time
import urllib.request
from quotetutorial.items import QuoteItem
# from quotetutorial.items import AuthorItem
from protego import Protego

'''
1.因为要将两个表数据整合
先将request库中的dontfilter参数设置成了True
使得about页面不被去重

2.将第一级页面的text，author，tags作为参数传递至about页面解析
数据yield至piplines中

3.自定义process_items函数生成csv文件
文件格式设置为gb18030
方便excel显示
若直接打开需设置为utf-8编码
'''
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']
    # start_urls = [f'http://quotes.toscrape.com/page/{page}/' for page in range(1,11)]

    def parse(self, response):
        quotes = response.css('.quote')

        for quote in quotes:
            text = quote.css('.text::text').extract_first()
            author = quote.css('.author::text').extract_first()
            tags = quote.css('.tags .tag::text').extract()
            # yield item

            #into 'about'
            about = quote.css('a::attr(href)').extract_first()
            about_url = response.urljoin(about)
            yield scrapy.Request(url = about_url, callback=lambda response, text=text,author=author,tags=tags: self.parse_author(response,text,author,tags))

        #next page
        next = response.css('.pager .next a::attr(href)').extract_first()
        if next:
            next_url = response.urljoin(next)
            yield scrapy.Request(url=next_url, callback=self.parse)

    #text,author,tags is from parse
    def parse_author(self, response, text,author,tags):
        author_details = response.css('.container .author-details')

        item = QuoteItem()
        item['text'] = text
        item['author'] = author
        item['tags'] = ','.join(tags)

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


