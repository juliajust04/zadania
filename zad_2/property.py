class Property:
    def __init__(
        self,
        area: float,
        rooms: int,
        price: float,
        address: str
    ):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self) -> str:
        return (
            f"Powierzchnia: {self.area} m2, "
            f"Pokoje: {self.rooms}, "
            f"Cena: {self.price} zł, "
            f"Adres: {self.address}"
        )
