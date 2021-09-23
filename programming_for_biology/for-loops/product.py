#!/usr/bin/env python3
from functools import reduce
from operator import mul


def get_product(numbers: list) -> int:
    return reduce(mul, numbers, 1)


def get_product_from_needle_on(numbers: list, needle: int) -> int:
    index = numbers.index(needle)
    return get_product(numbers[index:])


if __name__ == "__main__":
    numbers = [5, 7, 2, 9, 8, 9, 3, 4, 2, 3, 2, 7, 7, 5]
    print(f"Product: {get_product(numbers)}")
    print(f"Product from 3 on: {get_product_from_needle_on(numbers, 3)}")
