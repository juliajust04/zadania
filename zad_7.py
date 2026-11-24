from math import isqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for number in range(2, isqrt(n) + 1):
        if n % number == 0:
            return False

    return True