class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    @staticmethod
    def class_info():
        return 'Klasa opisująca posiadłość/nieruchomość'