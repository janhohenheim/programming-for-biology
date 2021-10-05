#!/usr/bin/env python3

import numpy.random as rd


def generate_coin_tosses():
    """
    Tosses a coin and returns 0 for heads and 1 for tails.
    """
    while True:
        yield rd.randint(0, 2)


def count_consecutives(tosses):
    """
    Counts the number of consecutive heads or tails.
    """
    consecutive_tosses = 1
    max_consecutive_tosses = 1
    for i in range(0, len(tosses) - 1):
        if tosses[i] == tosses[i + 1]:
            consecutive_tosses += 1
            max_consecutive_tosses = max(max_consecutive_tosses, consecutive_tosses)
        else:
            consecutive_tosses = 1
    return max_consecutive_tosses


def toss_until_we_get_consecutives(consecutive_tosses):
    """
    Tosses a coin until we get the number of consecutive tosses we want.
    """
    consecutive_tosses_so_far = 1
    last_toss = None
    for i, toss in enumerate(generate_coin_tosses()):
        if consecutive_tosses_so_far == consecutive_tosses:
            return i
        if last_toss == toss:
            consecutive_tosses_so_far += 1
        else:
            consecutive_tosses_so_far = 1
        last_toss = toss


if __name__ == "__main__":
    rd.seed(0)
    consecutive_tosses = 8
    rounds = toss_until_we_get_consecutives(consecutive_tosses)
    print(f"Got {consecutive_tosses} consecutive tosses in {rounds} rounds.")
