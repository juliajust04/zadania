def print_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)


numbers = list(range(1, 11))
print_even(numbers)
