import scrapy


class AfldataSpider(scrapy.Spider):
    name = "afldata"
    allowed_domains = ["afltables.com"]
    start_urls = ["http://afltables.com/"]

    def parse(self, response):
        pass
