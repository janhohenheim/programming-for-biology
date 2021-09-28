#!/usr/bin/env python3

import numpy.random as rd


def toss_coin(n):
    """
    Tosses a coin n times and returns 0 for heads and 1 for tails.
    """
    return rd.randint(0, 2, n)


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


def get_highest_consecutive_tosses(tosses):
    """
    Simulates tossing a coin n times and returns the number of consecutive heads or tails.
    """
    return count_consecutives(toss_coin(tosses))


if __name__ == "__main__":
    rd.seed(13)
    tosses = 1000
    highest_consecutive_tosses = get_highest_consecutive_tosses(tosses)
    print(
        f"After tossing a coint {tosses} times, the highest number of consecutive results was {highest_consecutive_tosses}"
    )
