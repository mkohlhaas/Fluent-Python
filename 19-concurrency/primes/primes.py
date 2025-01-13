#!/usr/bin/env python3

import math

PRIME_FIXTURE: list[tuple[int, bool]] = [
    (9999999999999999, False),
    (9999999999999917, True),
    (7777777777777777, False),
    (7777777777777753, True),
    (7777777536340681, False),
    (6666667141414921, False),
    (6666666666666719, True),
    (6666666666666666, False),
    (5555555555555555, False),
    (5555555555555503, True),
    (5555553133149889, False),
    (4444444488888889, False),
    (4444444444444444, False),
    (4444444444444423, True),
    (3333335652092209, False),
    (3333333333333333, False),
    (3333333333333301, True),
    (299593572317531, True),
    (142702110479723, True),
    (2, True),
]

NUMBERS = [n for n, _ in PRIME_FIXTURE]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    for n, is_prime_number in PRIME_FIXTURE:
        assert is_prime(n) == is_prime_number
        print(n, is_prime_number)
