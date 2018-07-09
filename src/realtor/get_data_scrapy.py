# -*- coding: utf-8 -*-
import scrapy


class RealtorScraper(scrapy.Spider):
    name = 'realtor.com houses'
    start_urls = [
        'https://www.realtor.com/realestateandhomes-search/Louisville_KY/type-single-family-home',
    ]

    def get_price(self, home_info):
        price_string: str = home_info.css('.data-price-display::text').extract_first()
        if price_string is None:
            return None
        _remove_chars = [',', '$']
        for char in _remove_chars:
            price_string = price_string.replace(char, '')
        return float(price_string)

    def get_rooms(self, home_info):
        room_string: str = home_info.css('li[data-label="property-meta-beds"] .data-value::text').extract_first()
        return float(room_string) if room_string else None

    def get_bathrooms(self, home_info):
        bath_string: str = home_info.css('li[data-label="property-meta-baths"] .data-value::text').extract_first()
        if bath_string is None:
            return None
        num_baths = float(bath_string.split('+')[0])
        if '+' in bath_string:
            num_baths = num_baths + 0.5
        return num_baths

    def get_lot(self, home_info):
        lot_string: str = home_info.css('li[data-label="property-meta-lotsize"] .data-value::text').extract_first()
        print(lot_string)
        size_info: str = home_info.css('li[data-label="property-meta-lotsize"]::text').extract_first()
        if 'acres' in size_info:
            lot_string = float(lot_string) * 43560
        return round(lot_string, 2)

    def parse(self, response):
        homes = []
        for home_info in response.css('.srp-item-body'):
            print(home_info)
            # print(self.get_lot(home_info))
        #     homes.append({
        #         'price': self.get_price(home_info),
        #         'num_rooms': self.get_rooms(home_info),
        #         'num_baths': self.get_bathrooms(home_info),
        #     })
        # print(homes)

        # next_page_url = response.css('.next .next::attr(href)').extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))
