"""
Zad 4.1
Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz jedną metodę is_passed, która zwraca wartość
logiczną, pozytywną gdy ocena jest > 50 w przeciwnym przypadku negatywną. Następnie należy stworzyć 2 przykładowe
obiekty klasy, tak aby dla pierwszego obiektu metoda zwracała true , a dla drugiego false .
"""
import datetime


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def compute_marks(self) -> bool:
        if self.marks > 50:
            return True
        else:
            return False


stud_1 = Student("John", 36)
stud_2 = Student("Adam", 51)
print("stud_1.compute_marks results:")
print(stud_1.compute_marks())
print("stud_2.compute_marks results:")
print(stud_2.compute_marks())

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


class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Adres biblioteki: {self.street}, {self.zip_code} {self.city} , godziny otwarcia {self.open_hours} , '\
               f'telefon kontaktowy: {self.phone} '

    @staticmethod
    def class_info():
        return 'Klasa opisująca biblioteke'


class Student:
    def __init__(self, first_name, last_name, birth_date: datetime.date, city, street, zip_code):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code

    def __str__(self):
        return f'Dane personalne studenta: {self.first_name} {self.last_name}, urodzony: '\
               f'{self.birth_date.strftime("%d-%m-%Y")}, zatrudniony: {self.birth_date.strftime("%d-%m-%Y")}, '\
               f'zamieszkały: {self.street} {self.zip_code} {self.city}'

    @staticmethod
    def class_info():
        return 'Klasa opisująca studenta'


class Employee:
    def __init__(self, first_name, last_name, hire_date: datetime.date, birth_date: datetime.date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Dane personalne pracownika: {self.first_name} {self.last_name}, urodzony: '\
               f'{self.birth_date.strftime("%d-%m-%Y")}, zatrudniony: {self.birth_date.strftime("%d-%m-%Y")}, '\
               f'zamieszkały: {self.street} {self.zip_code} {self.city}, tel kontaktowy: {self.phone}'

    @staticmethod
    def class_info():
        return 'Klasa opisująca pracownika'


class Order:
    def __init__(self, employee: Employee, student: Student, books, order_date: datetime.date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_info = ""
        for book in self.books:
            books_info += "\n"+book.__str__()

        return f'Dane zamówienia:\n{self.employee.__str__()}.\n{self.student.__str__()}. \nZamówione ksiązki: {books_info}'\
               f'\nData zamówienia {self.order_date.strftime("%d-%m-%Y")}.'

    @staticmethod
    def class_info():
        return 'Klasa opisująca zamówienie'


class Book:
    def __init__(self, title, library: Library, publication_date: datetime.date, author_name, author_surname, number_of_pages: int):
        self.title = title
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Tytuł: {self.title}. {self.library.__str__()}. Data publikacji: '\
               f'{self.publication_date.strftime("%d-%m-%Y")}, autor: {self.author_name} {self.author_surname}, '\
               f'liczba stron: {str(self.number_of_pages)}'

    @staticmethod
    def class_info():
        return 'Klasa opisująca książkę'


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
