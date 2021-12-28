#!/usr/bin/env python3
from pathlib import Path
from os.path import join
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Coordinates:
    x: float
    y: float

    def __str__(self) -> str:
        return f"(x: {self.x}, y: {self.y})"


@dataclass(frozen=True)
class Disc:
    polygons: List[List[int]]
    coordinates: List[Coordinates]

    def coordinates_of_polygon(self, index: int) -> Coordinates:
        return [self.coordinates[vertex] for vertex in self.polygons[index]]


def _get_code_dir():
    return Path(__file__).parent.absolute()


def _get_wingdisc_polygon_path(discname):
    directory = join(_get_code_dir(), "data", "wingdisc", discname)
    return (join(directory, "cv.txt"), join(directory, "vp.txt"))


def read_disc(discname) -> Disc:
    index_path, coordinate_path = _get_wingdisc_polygon_path(discname)
    with open(index_path) as index_file:
        with open(coordinate_path) as coordinate_file:
            polygons = [
                [int(index) for index in line.split()]
                for line in index_file.readlines()
            ]
            coordinates = [
                Coordinates(*line.split()) for line in coordinate_file.readlines()
            ]
            return Disc(polygons, coordinates)


if __name__ == "__main__":
    disc = read_disc("wd-large")
    for coordinates in disc.coordinates_of_polygon(0):
        print(coordinates)
