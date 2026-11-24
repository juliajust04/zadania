from zad_2.house import House
from zad_2.flat import Flat


if __name__ == "__main__":
    house = House(
        150.0,
        5,
        750000.0,
        "Bytom, ul. Dworcowa 10",
        500
    )

    flat = Flat(
        60.0,
        3,
        350000.0,
        "Katowice, ul. Mariacka 5",
        2
    )

    print(house)
    print(flat)
