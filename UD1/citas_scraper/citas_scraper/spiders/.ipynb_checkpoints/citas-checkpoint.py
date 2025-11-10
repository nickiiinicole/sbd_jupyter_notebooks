import scrapy


class CitasSpider(scrapy.Spider):
    name = "citas"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
            # Recorre todas las citas del bloque <div class="quote">
        for cita in response.css('div.quote'):
            yield {
                'texto': cita.css('span.text::text').get(),
                'autor': cita.css('small.author::text').get(),
                'tags': cita.css('div.tags a.tag::text').getall()
            }

        # Busca el enlace a la siguiente página
        next_page = response.css('li.next a::attr(href)').get()

        # Si existe, lo sigue
        if next_page:
            yield response.follow(next_page, callback=self.parse)
