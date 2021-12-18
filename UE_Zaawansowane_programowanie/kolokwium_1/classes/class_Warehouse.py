class Warehouse:
    def __init__(self, name: str, address: str, area: str, free_space: str, price_per_day: float):
        self.name = name
        self.address = address
        self.area = area
        self.free_space = free_space
        self.price_per_day = price_per_day

    def __str__(self):
        return f'Opis magazynu:\nNazwa: {self.name}\nPowierzchnia: {self.area}\nLokalizacja: {self.address}' \
               f'\nWolne miejsca: {self.free_space}\nCena za przechowanie (per dzień): {str(self.price_per_day)}'

    @property
    def get_name(self):
        print("Warehouse get name")
        return self.name

    @property
    def get_address(self):
        print("Warehouse get address")
        return self.address

    @property
    def get_area(self):
        print("Warehouse get area")
        return self.area

    @property
    def get_free_space(self):
        print("Warehouse get free_space")
        return self.free_space

    @property
    def get_price_per_day(self):
        print("Warehouse get price_per_day")
        return self.price_per_day

    @staticmethod
    def class_info():
        return 'Klasa opisująca magazyn'


# print(Warehouse("MAG_1", "Testowa 01 Katowice", "1000m2", "15 miejsc", 125.85).__str__())
