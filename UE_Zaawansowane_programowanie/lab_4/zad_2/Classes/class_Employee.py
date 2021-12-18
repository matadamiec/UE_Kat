from datetime import datetime


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
        return f'Dane personalne pracownika: {self.first_name} {self.last_name}, urodzony: ' \
               f'{self.birth_date.strftime("%d-%m-%Y")}, zatrudniony: {self.birth_date.strftime("%d-%m-%Y")}, ' \
               f'zamieszkały: {self.street} {self.zip_code} {self.city}, tel kontaktowy: {self.phone}'

    @staticmethod
    def class_info():
        return 'Klasa opisująca pracownika'
