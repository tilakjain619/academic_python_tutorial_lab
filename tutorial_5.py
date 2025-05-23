#Implement program to use scrapy python library for large scale web scrapping.

import scrapy
from scrapy.crawler import CrawlerProcess

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('article.product_pod'):
            item = {
                'title': book.css('h3 a::attr(title)').get(),
                'price': book.css('p.price_color::text').get(),
                'link': response.urljoin(book.css('h3 a::attr(href)').get()),
            }
            print(item)  # for me
            yield item

process = CrawlerProcess(settings={
    'USER_AGENT': 'MyScraper (+http://www.mysite.com)',
    'FEED_FORMAT': 'json',
    'FEED_URI': 'books.json',
    'LOG_LEVEL': 'INFO',
    'DOWNLOAD_DELAY': 1,
    'FEED_EXPORT_ENCODING': 'utf-8',
})

process.crawl(BooksSpider)
process.start()