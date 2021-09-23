#!/usr/bin/env python3


def add_up(n):
    """
    Adds up all numbers from 1 to n.
    """
    numbers = range(1, n + 1)
    return sum(numbers)


def add_even_up(n):
    """
    Adds up all numbers from 1 to n.
    """
    numbers = range(1, n + 1)
    even = [x for x in numbers if x % 2 == 0]
    return sum(even)


if __name__ == "__main__":
    print(f"sum: {add_up(213)}")
    print(f"sum of even: {add_even_up(226)}")
