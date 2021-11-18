#!/usr/bin/env python3
from pathlib import Path
from os.path import join
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np


def _get_code_dir():
    return Path(__file__).parent.absolute()


def read_jpg(filename):
    path = join(_get_code_dir(), "data", filename)
    return img.imread(path)


if __name__ == "__main__":
    image = read_jpg("hotspring_pattern.jpg")
    blue_right_boundary = image[:, -1, 2]
    average_blue_right_boundary = np.mean(blue_right_boundary)
    print(
        f"Average blue value of right boundary pixels: {np.mean(blue_right_boundary):.4}"
    )

    red_upper_boundary = image[0, :, 0]
    average_red_upper_boundary = np.mean(red_upper_boundary)
    print(
        f"Average red value of upper boundary pixels: {np.mean(red_upper_boundary):.4}"
    )
