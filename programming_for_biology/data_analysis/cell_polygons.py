#!/usr/bin/env python3
from pathlib import Path
from os.path import join
from dataclasses import dataclass, field
from typing import List
import weakref
from functools import reduce


@dataclass(frozen=True)
class Coordinates:
    x: float
    y: float

    def __str__(self) -> str:
        return f"(x: {self.x}, y: {self.y})"


@dataclass(frozen=True)
class Vertex:
    index: int
    _coordinates: List[Coordinates]

    def coordinates(self) -> Coordinates:
        return self._coordinates[self.index]

    def x(self) -> float:
        return self.coordinates().x

    def y(self) -> float:
        return self.coordinates().y


@dataclass(frozen=True)
class Polygon:
    vertices: List[Vertex]
    _coordinates: List[Coordinates]

    def coordinates(self) -> List[Coordinates]:
        return [self._coordinates[vertex.index] for vertex in self.vertices]

    def area(self) -> float:
        return 0.5 * reduce(
            lambda area, i: area
            + (
                self.vertices[i].x() * self.vertices[i - 1].y()
                - self.vertices[i - 1].x() * self.vertices[i].y()
            ),
            range(len(self.vertices)),
            0,
        )


@dataclass(frozen=True)
class Disc:
    polygons: List[Polygon]
    coordinates: List[Coordinates]


def _get_code_dir():
    return Path(__file__).parent.absolute()


def _get_wingdisc_polygon_path(discname):
    directory = join(_get_code_dir(), "data", "wingdisc", discname)
    return (join(directory, "cv.txt"), join(directory, "vp.txt"))


def read_disc(discname) -> Disc:
    index_path, coordinate_path = _get_wingdisc_polygon_path(discname)
    with open(index_path) as index_file:
        with open(coordinate_path) as coordinate_file:

            coordinates = [
                Coordinates(*line.split()) for line in coordinate_file.readlines()
            ]
            polygons = [
                Polygon(
                    [Vertex(int(index), coordinates) for index in line.split()],
                    coordinates,
                )
                for line in index_file.readlines()
            ]
            return Disc(polygons, coordinates)


if __name__ == "__main__":
    disc = read_disc("wd-large")
    for coordinates in disc.polygons[0].coordinates():
        print(coordinates)
    print(disc.polygons[0].area())
