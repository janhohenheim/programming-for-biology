#!/usr/bin/env python3

import numpy.random as rd


def roll_dice(n):
    """
    Simulate rolling n dice.
    """
    return rd.randint(1, 7, n)


if __name__ == "__main__":
    rd.seed(141)
    results = roll_dice(30)
    sixes = [i for i in results if i == 6]
    print(f"Rolled {len(sixes)} sixes")
