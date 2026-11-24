def contains_number(numbers: list, number: int) -> bool:
    return number in numbers


result = contains_number([1, 2, 3, 4, 5], 3)
print(result)