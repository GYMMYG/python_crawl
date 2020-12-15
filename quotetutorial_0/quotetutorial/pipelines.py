# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from quotetutorial.items import QuoteItem
from quotetutorial.items import AuthorItem

class QuotetutorialPipeline:
    def __init__(self):
        self.aw = csv.writer(open('author_details.csv', 'w',newline='',encoding='utf-8'))
        self.aw.writerow(["author_title","born_year","born_date","born_country","born_city","description"])
        self.qw = csv.writer(open('quotes.csv', 'w',newline=''))
        self.qw.writerow(["author","text","tags"])

    def process_item(self, item, spider):
        if isinstance(item,QuoteItem):
            self.qw.writerow((item['author'],item['text'],item['tags']))
        elif isinstance(item,AuthorItem):
            self.aw.writerow((item['author_title'],item['born_year'],item['born_date'],item['born_country'],item['born_city'],item['description']))

        return item
