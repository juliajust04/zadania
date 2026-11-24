import magazine.utils


class Order:
    def __init__(self, number: int, total: float):
        self.number = number
        self.total = total

    def __str__(self) -> str:
        total = magazine.utils.format_price(self.total)
        return f"Zamówienie: {self.number}, wartość: {total}"
