from src.realtor.utils.helpers import (
    get_price,
    get_num_bedrooms,
    get_num_bathrooms,
    get_sqft,
    get_lot_size,
    get_zip_code,
    get_address,
)
from bs4 import BeautifulSoup
import pytest


@pytest.fixture
def house_info():
    house_html = '''
        <div class="srp-item-body" itemprop="description">
            <!-- <a href="/realestateandhomes-detail/8109-Parkshire-Ct_Louisville_KY_40220_M40506-53335?ex=KY603554581" class="srp-card-anchor-overlay"></a> -->
            <div class="srp-item-label margin-bottom-sm">
                <div class="label-wrapper">
                <span class="label label-green" data-label="property-label-new">New</span>

            </div>
            </div>
            <div class="srp-item-price" data-label="property-price">
            <span class="data-price-display">$334,900</span>
            </div>

            <div class="srp-item-address ellipsis" data-label="property-address">
            <a href="/realestateandhomes-detail/8109-Parkshire-Ct_Louisville_KY_40220_M40506-53335?ex=KY603554581">
                <span class="listing-street-address">8109 Parkshire Ct</span>,
                <span class="listing-city">Louisville</span>,
                <span class="listing-region">KY</span>
                <span class="listing-postal">40220</span>
            </a>
            </div>

            <div class="srp-item-neighborhood ellipsis link-tertiary hidden-xxs hidden-xs-small" data-label="property-neighborhood">
                <a href="/realestateandhomes-search/East-Louisville_Louisville_KY">East Louisville</a>
            </div>

            <div class="srp-item-type srp-item-tags ellipsis hidden-xs-small hidden-xxs" data-label="property-type">
                <span class="srp-property-type">Single Family Home</span>
            </div>

            <div class="srp-item-property-meta">
            <ul class="property-meta list-horizontal list-style-disc list-spaced">
                <li data-label="property-meta-beds"><span class="data-value meta-beds">4</span> bd</li>
                <li data-label="property-meta-baths"><span class="data-value">2+</span> ba</li>
                <li data-label="property-meta-sqft"><span class="data-value">3,065</span> sq ft</li>
                <li data-label="property-meta-lotsize"><span class="data-value">8,712</span> sq ft lot</li>
                <li data-label="property-meta-garage"><span class="data-value">2</span> car</li>
            </ul>
            </div>

            <div class="srp-item-broker ellipsis">
                <span>Brokered by </span>
                <span class="srp-item-broker-text-sm" data-label="property-broker">Keller Williams Realty Louisville</span>
            </div>

            <div class="srp-item-ldp-link">
            <a class="btn btn-default hidden-xs-small hidden-xxs" href="/realestateandhomes-detail/8109-Parkshire-Ct_Louisville_KY_40220_M40506-53335?ex=KY603554581">View details</a>
            <a class="btn before-contact js-no-listing-click" data-omtag="srp:card:lead" data-target="#srp-lead-modal[listing-id='603554581']"data-toggle="modal" href="javascript:void(0);">
                Contact Agent
            </a>
            <a class="btn btn-ghost-dark after-contact js-no-listing-click" data-omtag="srp:card:lead" data-target="#srp-lead-modal[listing-id='603554581']" data-toggle="modal" href="javascript:void(0);">
                Contacted
            </a>
            </div>
        </div>
    '''

    return BeautifulSoup(house_html, 'html5lib')


def test_it_should_get_price_from_house_data(house_info):
    assert 334900.0 == get_price(house_info)


def test_it_should_get_number_of_bedrooms_from_house_data(house_info):
    assert 4 == get_num_bedrooms(house_info)


def test_it_should_get_number_of_bathrooms_from_house_data(house_info):
    assert 2.5 == get_num_bathrooms(house_info)


def test_it_should_get_square_feet_from_house_data(house_info):
    assert 3065 == get_sqft(house_info)


def test_it_should_get_lot_size_from_house_data(house_info):
    assert 8712 == get_lot_size(house_info)


def test_it_should_get_zip_code_from_house_data(house_info):
    assert 40220 == get_zip_code(house_info)


def test_it_should_get_address_from_house_data(house_info):
    assert '8109 Parkshire Ct' == get_address(house_info)
