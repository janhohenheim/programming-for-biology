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

    def _reduce_area(self, area: float, index: int) -> float:
        current_vertex = self.vertices[index]
        last_vertex = self.vertices[index - 1]
        return area + (
            current_vertex.x() * last_vertex.y() - last_vertex.x() * current_vertex.y()
        )

    def area(self) -> float:
        return 0.5 * reduce(
            self._reduce_area,
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
                Coordinates(*[float(coordinate) for coordinate in line.split()])
                for line in coordinate_file.readlines()
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
    coords = [Coordinates(1, 1), Coordinates(2, 3), Coordinates(4, 2)]
    disc = Disc(
        [Polygon([Vertex(0, coords), Vertex(1, coords), Vertex(2, coords)], coords)],
        coords,
    )
    print("Area of test polygon:", disc.polygons[0].area())

    disc = read_disc("wd-large")
    print("Coordinates of first polygon:")
    for coordinates in disc.polygons[0].coordinates():
        print(coordinates)
    print("Area of first polygon:", disc.polygons[0].area())
    print("Area of second polygon:", disc.polygons[1].area())
    print("Area of last polygon:", disc.polygons[-1].area())
