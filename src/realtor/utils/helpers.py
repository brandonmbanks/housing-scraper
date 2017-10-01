def get_price(house_item):
    price_string = house_item.find('span', {'class': 'data-price-display'}).text
    _remove_chars = ['$', ',']
    for char in _remove_chars:
        price_string = price_string.replace(char, '')
    return float(price_string)


def get_num_bedrooms(house_item):
    info = house_item.find('li', {'data-label': 'property-meta-beds'})
    if info is None:
        return None
    return float(info.span.text)


def get_num_bathrooms(house_item):
    info = house_item.find('li', {'data-label': 'property-meta-baths'})
    if info is None:
        return None
    if info.span.text[-1] == '+':
        return float(info.span.text[:-1]) + .5
    return float(info.span.text)


def get_sqft(house_item):
    info = house_item.find('li', {'data-label': 'property-meta-sqft'})
    if info is None:
        return None
    return float(info.span.text.replace(',', ''))


def get_lot_size(house_item):
    info = house_item.find('li', {'data-label': 'property-meta-lotsize'})
    if info is None:
        return None
    if 'acre' in info.text:
        # convert acres to sq ft
        return round(float(info.span.text.replace(',', '')) * 43560.0, 1)
    return float(info.span.text.replace(',', ''))


def get_zip_code(house_item):
    info = house_item.find('span', {'class': 'listing-postal'})
    if info is None:
        return None
    return int(info.text)


def get_address(house_item):
    info = house_item.find('span', {'class': 'listing-street-address'})
    if info is None:
        return None
    return info.text
