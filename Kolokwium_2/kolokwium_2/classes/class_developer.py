class Developer:
    def __init__(self, company_name: str, company_address: str, employees_number: int, share_capital: float, krs: str):
        self._company_name = company_name
        self._company_address = company_address
        self._employees_number = employees_number
        self._share_capital = share_capital
        self._krs = krs

    def __str__(self):
        return f'#Dane dewelopera#\nNazwa firmy: {self._company_name}\nAdres firmy: {self._company_address}' \
               f'\nLiczba pracowników: {str(self._employees_number)}\nKapitał zakładowy {str(self._share_capital)}\nNumer KRS: {self._krs}'

    @property
    def dev_company_name(self):
        return self._company_name

    @dev_company_name.setter
    def dev_company_name(self, value: str) -> None:
        self._company_name = value

    @property
    def dev_company_address(self):
        return self._company_address

    @dev_company_address.setter
    def dev_company_address(self, value: str) -> None:
        self._company_address = value

    @property
    def dev_employees_number(self):
        return self._employees_number

    @dev_employees_number.setter
    def dev_employees_number(self, value: int) -> None:
        self._employees_number = value

    @property
    def dev_share_capital(self):
        return self._share_capital

    @dev_share_capital.setter
    def dev_share_capital(self, value: float) -> None:
        self._share_capital = value

    @property
    def dev_krs(self):
        return self._krs

    @dev_krs.setter
    def dev_krs(self, value: str) -> None:
        self._krs = value

    @staticmethod
    def class_info():
        return 'Klasa opisująca dewelopera'
