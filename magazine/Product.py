import magazine.utils


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        price = magazine.utils.format_price(self.price)
        return f"Produkt: {self.name}, cena: {price}"
