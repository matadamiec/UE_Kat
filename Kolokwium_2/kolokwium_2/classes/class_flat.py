class Flat:
    def __init__(self, area: float, rooms_number: int, floor: int, building_side: str, price_per_m2: float, has_garden: bool):
        self._area = area
        self._rooms_number = rooms_number
        self._floor = floor
        self._building_side = building_side
        self._price_per_m2 = price_per_m2
        self._has_garden = has_garden

    def __str__(self):
        return f'#Opis mieszkania#\nPowierzchnia: {str(self._area)} m2\nLiczba pokoi: {str(self._rooms_number)}\nPiętro: {str(self._floor)}' \
               f'\nMieszkanie na stronie: {self._building_side}' \
               f'\nCena za m2: {str(self._price_per_m2)}' \
               f'\nOgródek: {"Tak" if self._has_garden == True else "Nie"}'

    @property
    def flat_area(self):
        return self._area

    @flat_area.setter
    def flat_area(self, value: float) -> None:
        self._area = value

    @property
    def flat_rooms_number(self):
        return self._rooms_number

    @flat_rooms_number.setter
    def flat_rooms_number(self, value: int) -> None:
        self._rooms_number = value

    @property
    def flat_floor(self):
        return self._floor

    @flat_floor.setter
    def flat_floor(self, value: int) -> None:
        self._floor = value

    @property
    def flat_building_side(self):
        return self._building_side

    @flat_building_side.setter
    def flat_building_side(self, value: str) -> None:
        self._building_side = value

    @property
    def flat_price_per_m2(self):
        return self._price_per_m2

    @flat_price_per_m2.setter
    def flat_price_per_m2(self, value: float) -> None:
        self._price_per_m2 = value

    @property
    def flat_has_garden(self):
        return self._has_garden

    @flat_has_garden.setter
    def flat_has_garden(self, value: bool) -> None:
        self._has_garden = value

    @staticmethod
    def class_info():
        return 'Klasa opisująca mieszkanie'
