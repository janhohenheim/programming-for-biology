#!/usr/bin/env python3

import numpy.random as rd


def roll_dice(n):
    """
    Simulate rolling n dice.
    """
    return rd.randint(1, 7, n)


def count_sixes(results):
    """
    Count the number of sixes in a list of integers.
    """
    return sum(1 for roll in results if roll == 6)


def simulate_dice_game(rolls_per_round, rounds):
    """
    Simulate rolling dice and counting sixes.
    """
    return [count_sixes(roll_dice(rolls_per_round)) for _ in range(rounds)]


if __name__ == "__main__":
    rd.seed(141)

    rolls_per_round = 30
    rounds = 10
    results = simulate_dice_game(rolls_per_round, rounds)
    print(results)
