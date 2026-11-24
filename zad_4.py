def print_every_second(numbers):
    for number in numbers[::2]:
        print(number)


numbers = list(range(1, 11))
print_every_second(numbers)
