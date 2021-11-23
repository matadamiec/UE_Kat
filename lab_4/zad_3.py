"""
Stworzyć następujące klasy:
Property (klasa opisująca posiadłość/nieruchomość), posiadająca pola:
    area
    rooms (int)
    price
    address
House (klasa dziedzicząca klasę Property , która opisuje dom), posiadająca pola:
    plot (rozmiar działki, int)
Flat (klasa dziedzicząca klasę Property , która opisuje mieszkanie), posiadająca pola:
    floor
Dodatkowo:
Każda z klas dziedziczących ma mieć zaimplementowaną metodę __str__ , która będzie opisywała obiekt.
Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas tworzenia instancji klasy za pośrednictwem
konstruktora.
Stworzyć po jednym obiekcie klasy House oraz Flat, a następnie je wyświetlić.
"""


class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    @staticmethod
    def class_info():
        return 'Klasa opisująca posiadłość/nieruchomość'


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'Opis domu:\nPowierzchnia: {self.area}\nLiczba pokoi: {self.rooms}\nCena: {self.price}\nLokalizacja: {self.address}'\
               f'\nRozmiar działki: {str(self.plot)}'

    @staticmethod
    def class_info():
        return 'Klasa opisująca dom'


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Opis mieszkania:\nPowierzchnia: {self.area}\nLiczba pokoi: {str(self.rooms)}\nCena: {self.price}\nLokalizacja: {self.address}'\
               f'\nPiętro: {str(self.floor)}'

    @staticmethod
    def class_info():
        return 'Klasa opisująca mieszkanie'


sample_house = House("180m2", 6, "760000", "Ul. Testowa 10/2 40-866 Katowice", 1500)
print(sample_house.__str__())
sample_flat = Flat("91m2", 4, "520000", "Ul. Rolna 28/4 40-530 Katowice", 4)
print(sample_flat.__str__())
