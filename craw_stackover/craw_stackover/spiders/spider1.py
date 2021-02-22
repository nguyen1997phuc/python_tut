import scrapy


class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    allowed_domains = ['http://vnstockfilter.com/']
    start_urls = ['http://vnstockfilter.com/']

    def parse(self, response):
        pass
