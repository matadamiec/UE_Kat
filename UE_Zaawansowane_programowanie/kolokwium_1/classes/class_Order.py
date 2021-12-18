import datetime

from kolokwium_1.classes.class_BusinessClient import BusinessClient
from kolokwium_1.classes.class_Product import Product
from kolokwium_1.classes.class_RetailClient import RetailClient


class Order:
    def __init__(self, order_id: str, order_date: datetime.datetime, ordered_products: [Product], retail_client: RetailClient,
                 business_client: BusinessClient):
        self._order_id = order_id
        self._order_date = order_date
        self._ordered_products = ordered_products
        self._retail_client = retail_client
        self._business_client = business_client

    def get_order_id(self):
        return self._order_id

    def set_order_id(self, order_id):
        self._order_id = order_id

    def get_order_date(self):
        return self._order_date

    def set_order_date(self, order_date):
        self._order_date = order_date

    def get_ordered_products(self):
        return self._ordered_products

    def set_ordered_products(self, ordered_products):
        self._ordered_products = ordered_products

    def get_retail_client(self):
        return self._retail_client

    def set_retail_client(self, retail_client):
        self._retail_client = retail_client

    def get_business_client(self):
        return self._business_client

    def set_business_client(self, business_client):
        self._business_client = business_client

    def calculate_sum_price(self):
        order_sum = 0
        for product in self._ordered_products:
            order_sum += product.price
        return order_sum

    def list_product(self):
        products_list = ""
        for product in self._ordered_products:
            products_list += product.__str__() + '\n'
        return products_list

    def __str__(self):
        return f'Dane zamówienia:\nNumer zamówienia: {self._order_id}\nData zamówienia: {str(self._order_date)}' \
               f'\nZamówione produkty: {self.list_product()}' \
               f'\nKlient detaliczny: {self._retail_client.__str__()}\nKlient biznesowy: {self._business_client.__str__()}' \
               f'\nWartość zamówienia: {str(self.calculate_sum_price())}'
