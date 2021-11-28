class RetailClient:
    def __init__(self, name: str, surname: str, address: str, phone: str, discount: float):
        self.name = name
        self.surname = surname
        self.address = address
        self.phone = phone
        self.discount = discount

    def __str__(self):
        return f'Dane klienta detalicznego:\nImie: {self.name}\nNazwisko: {self.surname}\nAdres: {self.address}' \
               f'\nNr telefonu: {self.phone}\nObniżka: {str(self.discount)}'

    @property
    def get_name(self):
        print("Retail Client get name")
        return self.name

    @property
    def get_surname(self):
        print("Retail Client get surname")
        return self.surname

    @property
    def get_address(self):
        print("Retail Client get address")
        return self.address

    @property
    def get_phone(self):
        print("Retail Client get phone")
        return self.phone

    @property
    def get_discount(self):
        print("Retail Client get discount")
        return self.discount

    @staticmethod
    def class_info():
        return 'Klasa opisująca klienta detalicznego'
