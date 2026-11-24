class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (
            f"Powierzchnia: {self.area} m2, "
            f"liczba pokoi: {self.rooms}, "
            f"cena: {self.price} zł, "
            f"adres: {self.address}"
        )


class House(Property):
    def __init__(self, area, rooms, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"Dom: {super().__str__()}, "
            f"powierzchnia działki: {self.plot} m2"
        )


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Mieszkanie: {super().__str__()}, piętro: {self.floor}"


house = House(150, 5, 750000, "Bytom, Polna 10", 800)
flat = Flat(60, 3, 350000, "Katowice, Szkolna 5", 2)

print(house)
print(flat)