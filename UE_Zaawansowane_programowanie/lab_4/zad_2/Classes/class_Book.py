from datetime import datetime

from lab_4.zad_2.Classes.class_Library import Library


class Book:
    def __init__(self, title, library: Library, publication_date: datetime.date, author_name, author_surname, number_of_pages: int):
        self.title = title
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Tytuł: {self.title}. {self.library.__str__()}. Data publikacji: ' \
               f'{self.publication_date.strftime("%d-%m-%Y")}, autor: {self.author_name} {self.author_surname}, ' \
               f'liczba stron: {str(self.number_of_pages)}'

    @staticmethod
    def class_info():
        return 'Klasa opisująca książkę'
