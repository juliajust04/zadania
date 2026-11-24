def merge_and_cube(list1: list, list2: list) -> list:
    merged = list1 + list2
    unique = sorted(set(merged))
    return [number ** 3 for number in unique]


result = merge_and_cube([1, 2, 3], [3, 4, 5])
print(result)