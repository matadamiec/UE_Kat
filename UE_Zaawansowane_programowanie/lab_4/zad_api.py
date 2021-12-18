import datetime

import requests
import json


response = requests.get("https://api.openbrewerydb.org/breweries")


def format_json(json_object):
    # create a formatted string of the Python JSON object
    text = json.dumps(json_object, sort_keys=True, indent=4)
    return text


class Brewery:
    def __init__(self, address_2, address_3, brewery_type, city, country, county_province, created_at: datetime.datetime, id, latitude: float,
                 longitude: float, name, phone, postal_code, state, street, updated_at: datetime.datetime, website_url):
        self.address_2 = address_2
        self.address_3 = address_3
        self.brewery_type = brewery_type
        self.city = city
        self.country = country
        self.county_province = county_province
        self.created_at = created_at
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.phone = phone
        self.postal_code = postal_code
        self.state = state
        self.street = street
        self.updated_at = updated_at
        self.website_url = website_url


jsonStr = format_json(response.json())
objects_from_json = json.loads(jsonStr)
print(objects_from_json[0])
