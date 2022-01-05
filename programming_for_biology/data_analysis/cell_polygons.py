#!/usr/bin/env python3
from pathlib import Path
from os.path import join
from dataclasses import dataclass
from typing import Callable, List
from functools import reduce
import numpy as np


@dataclass(frozen=True)
class Coordinates:
    x: float
    y: float

    def center():
        return Coordinates(0, 0)

    def __str__(self) -> str:
        return f"(x: {self.x}, y: {self.y})"

    def distance_to(self, other: "Coordinates") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


@dataclass(frozen=True)
class Vertex:
    index: int
    _coordinates: List[Coordinates]

    def __str__(self) -> str:
        return f"Vertex {self.index}: {self.coordinates()}"

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

    def __str__(self) -> str:
        return f"{self.vertices}"

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

    def _reduce_centroid_x(self, centroid: float, index: int) -> Coordinates:
        current_vertex = self.vertices[index]
        last_vertex = self.vertices[index - 1]
        return centroid + (
            (current_vertex.x() + last_vertex.x())
            * (
                current_vertex.x() * last_vertex.y()
                - last_vertex.x() * current_vertex.y()
            )
        )

    def _curry_reduce_centroid(
        self, get_a: Callable[[Vertex], float], get_b: Callable[[Vertex], float]
    ) -> Coordinates:
        def _reduce_centroid(centroid: float, index: int) -> Coordinates:
            current_vertex = self.vertices[index]
            last_vertex = self.vertices[index - 1]
            return centroid + (
                (get_a(current_vertex) + get_a(last_vertex))
                * (
                    get_a(current_vertex) * get_b(last_vertex)
                    - get_a(last_vertex) * get_b(current_vertex)
                )
            )

        return _reduce_centroid

    def _get_centroid_coordinate(
        self, get_a: Callable[[Vertex], float], get_b: Callable[[Vertex], float]
    ) -> float:
        factor = -1.0 / (6.0 * self.area())
        return factor * reduce(
            self._curry_reduce_centroid(get_a, get_b),
            range(len(self.vertices)),
            0.0,
        )

    def centroid(self) -> Coordinates:
        x = self._get_centroid_coordinate(Vertex.x, Vertex.y)
        y = self._get_centroid_coordinate(Vertex.y, Vertex.x)
        return Coordinates(x, y)


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

    areas = [polygon.area() for polygon in disc.polygons]
    distances = [
        polygon.centroid().distance_to(Coordinates.center())
        for polygon in disc.polygons
    ]

    print("Area of first polygon:", areas[0])
    print("Area of second polygon:", areas[1])
    print("Area of last polygon:", areas[-1])

    print("Centroid of first polygon:", disc.polygons[0].centroid())
    print(
        "Distance to center",
        distances[0],
    )

    print("Centroid of second polygon:", disc.polygons[1].centroid())
    print(
        "Distance to center",
        distances[1],
    )
