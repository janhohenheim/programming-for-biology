#!/usr/bin/env python3
from functools import reduce


def factorial(n: int):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)


if __name__ == "__main__":
    print(factorial(19))
