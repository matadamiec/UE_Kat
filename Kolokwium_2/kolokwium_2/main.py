from kolokwium_2.classes.class_developer import Developer
from kolokwium_2.classes.class_flat import Flat
from kolokwium_2.classes.class_house import House
from kolokwium_2.classes.class_order import Order

Developer1 = Developer("Urbexim", "Katowice ul. Kościuszki", 1000, 2800350, "0908070605")

Flat1 = Flat(72.5, 3, 0, "Północny/Wschód", 5450.53, False)
Flat2 = Flat(109, 5, 0, "Południe/Wschód", 5200.99, True)
Flat3 = Flat(95, 4, 0, "Południe/Zachód", 5298.12, True)

# def __init__(self, area: float, rooms_number: int, floors: int, price_per_m2: float, garden_area: float, has_garage: bool):
House1 = House(125, 7, 0, 6700, 450, False)
House2 = House(145, 8, 0, 6950, 730, False)
House3 = House(155, 9, 1, 7150, 890, True)

Order1 = Order()
Order1.order_id = "Zamówienie 1"
Order1.order_developer = Developer1
Order1.order_ordered_flats = [Flat1, Flat2, Flat3]
Order1.order_ordered_houses = [House1, House2, House3]
print("Suma zamówienia: "+str(Order1.order_sum()))
print("Suma powierzchni: "+str(Order1.area_sum()))
