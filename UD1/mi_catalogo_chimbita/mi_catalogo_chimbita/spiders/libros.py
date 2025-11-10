import scrapy


class LibrosSpider(scrapy.Spider):
    name = "libros"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        pass
