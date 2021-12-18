from datetime import datetime


class Student:
    def __init__(self, first_name, last_name, birth_date: datetime.date, city, street, zip_code):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code

    def __str__(self):
        return f'Dane personalne studenta: {self.first_name} {self.last_name}, urodzony: ' \
               f'{self.birth_date.strftime("%d-%m-%Y")}, zatrudniony: {self.birth_date.strftime("%d-%m-%Y")}, ' \
               f'zamieszkały: {self.street} {self.zip_code} {self.city}'

    @staticmethod
    def class_info():
        return 'Klasa opisująca studenta'
