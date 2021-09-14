#!/usr/bin/env python3

import numpy as np


def _validate_recombination_frequency(recombination_frequency: float):
    if recombination_frequency < 0.0 or recombination_frequency >= 0.5:
        raise ValueError(
            f"recombination_frequency must be in the range [0.0, 0.5), but is {recombination_frequency}"
        )


def get_map_distance(recombination_frequency: float) -> float:
    """
    Returns the distance in cM between two genes.
    """
    _validate_recombination_frequency(recombination_frequency)

    return -0.5 * np.log(1 - 2 * recombination_frequency)


if __name__ == "__main__":
    map_distance = get_map_distance(0.115)
    print(map_distance)
