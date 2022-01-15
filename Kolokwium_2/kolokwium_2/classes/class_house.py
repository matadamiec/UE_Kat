class House:
    def __init__(self, area: float, rooms_number: int, floors: int, price_per_m2: float, garden_area: float, has_garage: bool):
        self._area = area
        self._rooms_number = rooms_number
        self._floors = floors
        self._price_per_m2 = price_per_m2
        self._garden_area = garden_area
        self._has_garage = has_garage

    def __str__(self):
        return f'#Opis domu#\nPowierzchnia: {self._area}\nLiczba pokoi: {str(self._rooms_number)}\nLiczba pięter: {str(self._floors)}' \
               f'\nCena za m2: {str(self._price_per_m2)}' \
               f'\nPowierzchnia ogrodu: {str(self._garden_area)} m2' \
               f'\nGaraż: {"Tak" if self._has_garage == True else "Nie"}'

    @property
    def house_area(self):
        return self._area

    @house_area.setter
    def house_area(self, value: float) -> None:
        self._area = value

    @property
    def house_rooms_number(self):
        return self._rooms_number

    @house_rooms_number.setter
    def house_rooms_number(self, value: int) -> None:
        self._rooms_number = value

    @property
    def house_floors(self):
        return self._floors

    @house_floors.setter
    def house_floors(self, value: int) -> None:
        self._floors = value

    @property
    def house_price_per_m2(self):
        return self._price_per_m2

    @house_price_per_m2.setter
    def house_price_per_m2(self, value: float) -> None:
        self._price_per_m2 = value

    @property
    def house_garden_area(self):
        return self._garden_area

    @house_garden_area.setter
    def house_garden_area(self, value: float) -> None:
        self._garden_area = value

    @property
    def house_has_garage(self):
        return self._has_garage

    @house_has_garage.setter
    def house_has_garage(self, value: bool) -> None:
        self._has_garage = value

    @staticmethod
    def class_info():
        return 'Klasa opisująca dom'
