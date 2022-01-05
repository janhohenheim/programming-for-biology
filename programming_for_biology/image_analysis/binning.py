#!/usr/bin/env python3
import numpy as np

if __name__ == "__main__":
    ar = (
        np.array(
            [
                0.3,
                0.2,
                0.4,
                0.1,
                0.5,
                0.5,
                0.7,
                1.0,
                0.3,
                0.3,
                0.2,
                0.1,
                0.8,
                0.8,
                0.7,
                0.6,
                0.3,
                0.0,
                0.1,
                0.2,
                0.7,
                0.4,
            ]
        )
        ** 2
    )
    window = 0.2
    applied_window = np.copy(ar)
    for i in range(int(max(ar) / window) + 2):
        applied_window[(i * window <= ar) & (ar < (i + 1) * window)] = i
    count = np.bincount(applied_window.astype(int))
    print(count)

    sex = np.array([0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0])  # male: 0; female: 1
    height = np.array(
        [
            1.83,
            1.72,
            1.61,
            1.68,
            1.79,
            1.75,
            1.92,
            1.76,
            1.66,
            1.68,
            1.69,
            1.61,
            1.70,
            1.78,
        ]
    )  # in meters
    total_sexes = np.bincount(sex)
    total_heights = np.bincount(sex, height)
    averages = total_heights / total_sexes
    male_delta = (averages[0] - averages[1]) * 100
    print(f"Mean are on average {male_delta} cm taller than women")
