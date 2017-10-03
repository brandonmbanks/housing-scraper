from urllib.request import HTTPCookieProcessor, build_opener
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randint
import os
from utils.helpers import (
    get_price,
    get_num_bedrooms,
    get_num_bathrooms,
    get_sqft,
    get_lot_size,
    get_zip_code,
    get_address,
)


def create_csv(houses):
    df = pd.DataFrame(houses)
    df.to_csv('{}/data.csv'.format(os.path.dirname(os.path.abspath(__file__))), index=False)


pageNumber = '1'
url = 'https://www.realtor.com/realestateandhomes-search/Louisville_KY/pg-{}'.format(pageNumber)
opener = build_opener(HTTPCookieProcessor)
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')]
page = opener.open(url)
# request = Request(url=url, headers={'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})
# page = urlopen(request)

soup = BeautifulSoup(page, 'html5lib')
last_page = int(soup.select('a[data-omtag*=srp:paging:]')[1].text)
print('last page: {}'.format(last_page))

houses: list = []

for i in range(1, last_page + 1):
    print(i)
    url = 'https://www.realtor.com/realestateandhomes-search/Louisville_KY/pg-{}'.format(i)
    try:
        if i % 2 == 0:
            sleep(randint(15, 30))
        opener = build_opener(HTTPCookieProcessor)
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')]
        page = opener.open(url)
    except Exception as e:
        print(str(e))
        create_csv(houses)
        break

    soup = BeautifulSoup(page, 'html5lib')

    house_info_list = soup.find_all('div', {'class': 'srp-item-body'})

    for house_info in house_info_list:
        houses.append({
            'price': get_price(house_info),
            'num_bedrooms': get_num_bedrooms(house_info),
            'num_bathrooms': get_num_bathrooms(house_info),
            'sqft': get_sqft(house_info),
            'lot_size': get_lot_size(house_info),
            'address': get_address(house_info),
            'zip_code': get_zip_code(house_info),
        })
        print(houses[-1])

df = pd.DataFrame(houses)
df.to_csv('{}/data-2.csv'.format(os.path.dirname(os.path.abspath(__file__))), index=False, mode='a', header=False)

print('done')
