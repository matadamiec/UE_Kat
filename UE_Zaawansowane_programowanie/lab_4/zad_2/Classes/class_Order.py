from datetime import datetime

from lab_4.zad_2.Classes.class_Book import Book
from lab_4.zad_2.Classes.class_Employee import Employee
from lab_4.zad_2.Classes.class_Student import Student


class Order:
    def __init__(self, employee: Employee, student: Student, books: [Book], order_date: datetime.date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_info = ""
        for book in self.books:
            books_info += "\n" + book.__str__()

        return f'Dane zamówienia:\n{self.employee.__str__()}.\n{self.student.__str__()}. \nZamówione ksiązki: {books_info}' \
               f'\nData zamówienia {self.order_date.strftime("%d-%m-%Y")}.'

    @staticmethod
    def class_info():
        return 'Klasa opisująca zamówienie'
