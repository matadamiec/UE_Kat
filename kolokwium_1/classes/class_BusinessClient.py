class BusinessClient:
    def __init__(self, company_name: str, company_address: str, representative_name: str, representative_surname: str, phone: str):
        self.company_name = company_name
        self.company_address = company_address
        self.representative_name = representative_name
        self.representative_surname = representative_surname
        self.phone = phone

    def __str__(self):
        return f'Dane klienta Biznesowego:\nNazwa firmy: {self.company_name}\nAdres firmy: {self.company_address}' \
               f'\nPrzedstawiciel: {self.representative_name} {self.representative_surname}\nTelefon: {self.phone}'

    @property
    def get_company_name(self):
        print("Business Client get company name")
        return self.company_name

    @property
    def get_company_address(self):
        print("Retail Client get company address")
        return self.company_address

    @property
    def get_representative_name(self):
        print("Retail Client get representative name")
        return self.representative_name

    @property
    def get_representative_surname(self):
        print("Retail Client get representative surname")
        return self.representative_surname

    @property
    def get_phone(self):
        print("Retail Client get get_phone")
        return self.get_phone

    @staticmethod
    def class_info():
        return 'Klasa opisująca klienta biznesowego'
