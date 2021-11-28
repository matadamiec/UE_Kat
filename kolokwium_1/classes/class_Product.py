import class_Warehouse


class Product:
    def __init__(self, product_id: str, name: str, price: float, weight: float, measurements: str, storage: class_Warehouse.Warehouse):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.weight = weight
        self.measurements = measurements
        self.storage = storage

    def __str__(self):
        return f'Opis produktu:\nIdentyfikator: {self.product_id}\nNazwa: {self.name}\nCena: {str(self.price)}\nWaga: {str(self.weight)}' \
               f'\nWymiary: {self.measurements}\nMagazyn:{self.storage.__str__()}'

    @property
    def get_product_id(self):
        print("Product get product_id")
        return self.product_id

    @property
    def get_name(self):
        print("Product get name")
        return self.name

    @property
    def get_price(self):
        print("Product get price")
        return self.price

    @property
    def get_measurements(self):
        print("Product get measurements")
        return self.measurements

    @property
    def get_storage(self):
        print("Product get storage")
        return self.storage

    @staticmethod
    def class_info():
        return 'Klasa opisująca produkt'
