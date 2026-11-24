from zad_2.property import Property


class House(Property):
    def __init__(
        self,
        area: float,
        rooms: int,
        price: float,
        address: str,
        plot: int
    ):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self) -> str:
        return (
            f"Dom: {super().__str__()}, "
            f"Działka: {self.plot} m2"
        )
