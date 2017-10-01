from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd
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

pageNumber = '1'
url = 'https://www.realtor.com/realestateandhomes-search/40220/pg-{}'.format(pageNumber)
request = Request(url=url, headers={'User-agent': 'Mozilla/5.0'})
page = urlopen(request)

soup = BeautifulSoup(page, 'html5lib')
last_page = int(soup.select('a[data-omtag*=srp:paging:]')[1].text)

houses = []

for i in range(1, last_page + 1):
    print(i)
    url = 'https://www.realtor.com/realestateandhomes-search/40220/pg-{}'.format(i)
    request = Request(url=url, headers={'User-agent': 'Mozilla/5.0'})
    page = urlopen(request)

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

df = pd.DataFrame(houses)
df.to_csv('{}/data.csv'.format(os.path.dirname(os.path.abspath(__file__))), index=False)

print('done')
