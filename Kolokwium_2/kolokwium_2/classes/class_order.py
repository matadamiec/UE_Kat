from kolokwium_2.classes.class_developer import Developer
from kolokwium_2.classes.class_flat import Flat
from kolokwium_2.classes.class_house import House


class Order:
    def __init__(self):
        self._order_id = None
        self._developer: Developer = Developer("", "", 0, 0, "")
        self._ordered_flats: [Flat] = []
        self._ordered_houses: [House] = []

    def __str__(self):
        return f'#Dane zamówienia#\nId zamówienia: {self._order_id}\nDeweloper: {self._developer.__str__()}'

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value: str) -> None:
        self._order_id = value

    @property
    def order_developer(self):
        return self._developer

    @order_developer.setter
    def order_developer(self, value: Developer) -> None:
        self._developer = value

    @property
    def order_ordered_flats(self):
        return self._ordered_flats

    @order_ordered_flats.setter
    def order_ordered_flats(self, value: [Flat]) -> None:
        self._ordered_flats = value

    @property
    def order_ordered_houses(self):
        return self._ordered_houses

    @order_ordered_houses.setter
    def order_ordered_houses(self, value: [House]) -> None:
        self._ordered_houses = value

    def order_sum(self):
        order_value = float(0)
        for flat in self._ordered_flats:
            order_value += (flat.flat_area * flat.flat_price_per_m2)

        for house in self._ordered_houses:
            order_value += (house.house_area * house.house_price_per_m2)

        return round(order_value, 2)

    def area_sum(self):
        flat_area_sum = float(0)
        for flat in self._ordered_flats:
            flat_area_sum += flat.flat_area

        house_area_sum = float(0)
        for house in self._ordered_houses:
            house_area_sum += house.house_area

        return flat_area_sum+house_area_sum
