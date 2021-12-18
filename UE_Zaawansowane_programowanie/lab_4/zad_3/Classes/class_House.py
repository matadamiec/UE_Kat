from lab_4.zad_3.Classes.class_Property import Property


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'Opis domu:\nPowierzchnia: {self.area}\nLiczba pokoi: {self.rooms}\nCena: {self.price}\nLokalizacja: {self.address}' \
               f'\nRozmiar działki: {str(self.plot)}'

    @staticmethod
    def class_info():
        return 'Klasa opisująca dom'
