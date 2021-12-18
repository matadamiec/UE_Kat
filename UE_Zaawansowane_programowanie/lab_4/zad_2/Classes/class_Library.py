class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Adres biblioteki: {self.street}, {self.zip_code} {self.city} , godziny otwarcia {self.open_hours} , ' \
               f'telefon kontaktowy: {self.phone} '

    @staticmethod
    def class_info():
        return 'Klasa opisująca biblioteke'
