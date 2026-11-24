def multiply_for(numbers):
    result = []
    for number in numbers:
        result.append(number * 2)
    return result


def multiply_list(numbers):
    return [number * 2 for number in numbers]


numbers = [1, 2, 3, 4, 5]

print(multiply_for(numbers))
print(multiply_list(numbers))
