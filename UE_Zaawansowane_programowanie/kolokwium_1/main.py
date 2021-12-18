import datetime
from kolokwium_1.classes.class_Warehouse import Warehouse
from kolokwium_1.classes.class_Product import Product
from kolokwium_1.classes.class_RetailClient import RetailClient
from kolokwium_1.classes.class_BusinessClient import BusinessClient
from kolokwium_1.classes.class_Order import Order

warehouse1 = Warehouse("MAG_1", "Testowa 01 Katowice", "1000m2", "15 miejsc", 125.85)
warehouse2 = Warehouse("MAG_3", "Testowa 15 Warszawa", "2000m2", "150 miejsc", 1250.85)
product1 = Product("01", "Produkt_1", 25.99, 100, "10x20x30", warehouse1)
product2 = Product("02", "Produkt_2", 38.99, 50, "40x60x80", warehouse2)
retail_client = RetailClient("Mateusz", "Adamiec", "Testowa 50/4 Katowice", "100200300", 0.25)
business_client = BusinessClient("Kryptokopalnie Sp. z.o.o", "Ugabuga 15, Madagaskar", "Julian", "Król", "007007007")
sample_order = Order("ZAM_01_01_2021", datetime.datetime.now(), [product1, product2], retail_client, business_client)
print(sample_order.__str__())
