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
from lab_4.zad_3.Classes.class_Flat import Flat
from lab_4.zad_3.Classes.class_House import House

sample_house = House("180m2", 6, "760000", "Ul. Testowa 10/2 40-866 Katowice", 1500)
print(sample_house.__str__())
sample_flat = Flat("91m2", 4, "520000", "Ul. Rolna 28/4 40-530 Katowice", 4)
print(sample_flat.__str__())
