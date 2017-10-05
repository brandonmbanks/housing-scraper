# -*- coding: utf-8 -*-
import scrapy


class RealtorScraper(scrapy.Spider):
    name = 'realtor.com houses'
    start_urls = [
        'https://www.realtor.com/realestateandhomes-search/Louisville_KY/type-single-family-home',
    ]

    def parse(self, response):
        homes = []
        for home_info in response.css('.srp-item-body'):
            price_string: str = home_info.css('.data-price-display::text').extract_first()
            _remove_chars = [',', '$']
            for char in _remove_chars:
                price_string = price_string.replace(char, '')
            price = float(price_string)
            room_string: str = home_info.css('li[data-label="property-meta-beds"] .data-value::text').extract_first()
            num_rooms = float(room_string)
            bath_string: str = home_info.css('li[data-label="property-meta-baths"] .data-value::text').extract_first()
            num_baths = float(bath_string.split('+')[0])
            if '+' in bath_string:
                num_baths = num_baths + 0.5
            homes.append({
                'price': price,
                'num_rooms': num_rooms,
                'num_baths': num_baths,
            })
        print(homes)
        # for quote in response.css("div.quote"):
        #     yield {
        #         'text': quote.css("span.text::text").extract_first(),
        #         'author': quote.css("small.author::text").extract_first(),
        #         'tags': quote.css("div.tags > a.tag::text").extract()
        #     }

        # next_page_url = response.css('.next .next::attr(href)').extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))
