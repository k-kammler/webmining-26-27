import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes2"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("span small::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

# Aufruf im Terminal (nicht mit "python ..."):
# scrapy runspider example_crawler_2.py
# oder
# scrapy runspider example_crawler_2.py -O quotes.json
