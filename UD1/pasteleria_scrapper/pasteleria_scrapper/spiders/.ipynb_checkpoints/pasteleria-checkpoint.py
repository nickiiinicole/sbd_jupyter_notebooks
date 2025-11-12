import scrapy


class PasteleriaSpider(scrapy.Spider):
    name = "pasteleria"
    allowed_domains = ["elatelierdediegocaride.com"]
    start_urls = ["https://elatelierdediegocaride.com/15-pasteles"]

    def parse(self, response):
        
        productos=response.css("article.product-miniature")
    
        for producto in productos:    
            nombre=producto.css("h2.product-title a::text").get()
            precio=producto.css("span.price::text").get()

            yield{
                "nombre": nombre.strip(),
                "precio": precio.strip()
            }

             # Paginación
        siguiente = response.css("ul.page-list a::attr(href)").get()
        if siguiente:
            yield response.follow(siguiente, self.parse)