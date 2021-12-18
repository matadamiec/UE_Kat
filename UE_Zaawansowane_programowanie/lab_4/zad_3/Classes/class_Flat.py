from lab_4.zad_3.Classes.class_Property import Property


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Opis mieszkania:\nPowierzchnia: {self.area}\nLiczba pokoi: {str(self.rooms)}\nCena: {self.price}\nLokalizacja: {self.address}' \
               f'\nPiętro: {str(self.floor)}'

    @staticmethod
    def class_info():
        return 'Klasa opisująca mieszkanie'
