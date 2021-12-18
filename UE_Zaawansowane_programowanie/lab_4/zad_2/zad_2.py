"""
Stworzyć następujące klasy:

Library (klasa opisująca bibliotekę), posiadająca pola:
    -city
    -street
    -zip_code
    -open_hours (str)
    -phone
Order (klasa opisująca zamówienie), posiadająca pola:
    -employee
    -student
    -books
    -order_date
Employee (klasa opisująca pracownika biblioteki), posiadająca pola:
    -first_name
    -last_name
    -hire_date
    -birth_date
    -city
    -street
    -zip_code
    -phone
Book (klasa opisująca książkę), posiadająca pola
    -library
    -publication_date
    -author_name
    -author_surname
    -number_of_pages
Dodatkowo:
Każda klasa ma mieć zaimplementowaną metodę __str__ , która będzie opisywała obiekt oraz ewentualne obiekty
znajdujące się w tym obiekcie (np. obiekt Library w obiekcie Book).
Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas tworzenia instancji klasy za pośrednictwem
konstruktora.
Stworzyć 2 biblioteki (2 instancje klasy), 5 książek, 3 pracowników, 3 studentów, oraz 2 zamówienia.
Wyświetlić oba zamówienia ( print )
"""
import datetime
from lab_4.zad_2.Classes.class_Library import Library
from lab_4.zad_2.Classes.class_Student import Student
from lab_4.zad_2.Classes.class_Employee import Employee
from lab_4.zad_2.Classes.class_Book import Book
from lab_4.zad_2.Classes.class_Order import Order

first_library = Library('Katowice', 'ul. Wodospady', '40-556', '7-17', '100200300')
second_library = Library('Chorzów', 'ul. Dębowa', '40-600', '11-20', '900800700')
first_book = Book("Sam naprawiam", first_library, datetime.date(2021, 1, 10), "Jacek", "Bąk", 100)
second_book = Book("Gotuje z Makłowiczem", second_library, datetime.date(2021, 3, 14), "Wacek", "Gniot", 200)
third_book = Book("Jedz z Geslerową", second_library, datetime.date(2021, 6, 23), "Placek", "Wegierski", 300)
fourth_book = Book("Smaż z Pascalem", second_library, datetime.date(2021, 8, 1), "Horacy", "Dopracy", 400)
fifth_book = Book("Podstawy Pyhona", first_library, datetime.date(2021, 10, 24), "Eustachy", "Buc", 500)
first_employee = Employee("Kuba", "Buba", datetime.date(2019, 1, 1), datetime.date(1975, 12, 6), "Katowice", "Kościuszki", "40-200", "101102103")
second_employee = Employee("Maciej", "Szczur", datetime.date(2020, 10, 11), datetime.date(1999, 6, 1), "Warszawa", "Armii Krajowej", "34-123", "201202203")
third_employee = Employee("Tomasz", "Pies", datetime.date(2007, 7, 10), datetime.date(1989, 7, 28), "Wrocław", "Fabryczna", "28-699", "301302303")
first_student = Student("Student", "Pierwszy", datetime.date(1991, 1, 1), "Poznań", "Słoneczna", "11-111")
second_student = Student("Student", "Drugi", datetime.date(1992, 2, 2), "Gdynia", "Morska", "22-222")
third_student = Student("Student", "Trzeci", datetime.date(1993, 3, 3), "Sopot", "Festiwalowa", "33-333")
first_order = Order(first_employee, second_student, [first_book, second_book], datetime.date(2021, 11, 12))
second_order = Order(third_employee, third_student, [third_book, fourth_book, fifth_book], datetime.date(2021, 11, 16))


print(first_order.__str__())
print(second_order.__str__())
