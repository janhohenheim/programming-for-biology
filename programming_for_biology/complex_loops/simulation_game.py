#!/usr/bin/env python3

import numpy.random as rd


def guess_suits(cards):
    """
    Simulate a game of guessing the suit of a card.
    """
    return sum(1 for guess in rd.randint(0, 4, cards) if guess == 0)


def guess_rounds(cards_per_round, rounds):
    """
    Simulate a game of guessing the number of rounds for multiple rounds.
    """
    return (guess_suits(cards_per_round) for _ in range(rounds))


def count_guesses_above_hitrate(cards_per_round, rounds, hitrate):
    """
    Simulate a game of guessing the number of rounds for multiple rounds.
    Returns the number of rounds above the hitrate.
    """
    return sum(1 for guess in guess_rounds(cards_per_round, rounds) if guess >= hitrate)


if __name__ == "__main__":
    cards_per_round = 400
    rounds = 10_000
    hitrate = 117
    print(f"Playing {rounds} rounds with {cards_per_round} cards per round.")
    guesses_above_hitrate = count_guesses_above_hitrate(
        cards_per_round, rounds, hitrate
    )
    print(f"Got {guesses_above_hitrate} guesses above the hitrate of {hitrate}")
    probability = guesses_above_hitrate / rounds
    print(
        f"Therefore this getting at least this many guesses right has a chance of about: {probability * 100:.2f}%"
    )
