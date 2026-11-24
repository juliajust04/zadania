from zad_2.property import Property


class Flat(Property):
    def __init__(
        self,
        area: float,
        rooms: int,
        price: float,
        address: str,
        floor: int
    ):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self) -> str:
        return (
            f"Mieszkanie: {super().__str__()}, "
            f"Piętro: {self.floor}"
        )
