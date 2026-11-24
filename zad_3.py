def is_even(number: int) -> bool:
    return number % 2 == 0


result = is_even(8)

if result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
