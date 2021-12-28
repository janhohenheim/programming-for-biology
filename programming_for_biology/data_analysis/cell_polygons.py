#!/usr/bin/env python3
from pathlib import Path
from os.path import join
from dataclasses import dataclass, field
from typing import List
import weakref


@dataclass(frozen=True)
class Coordinates:
    x: float
    y: float

    def __str__(self) -> str:
        return f"(x: {self.x}, y: {self.y})"


class Polygon:
    pass


@dataclass
class Vertex:
    index: int
    _polygon: Polygon = field(init=False)

    def init_polygon(self, polygon: Polygon) -> None:
        self._polygon = weakref.proxy(polygon)

    def coordinates(self) -> Coordinates:
        return self._polygon._disc.coordinates[self.index]


class Disc:
    pass


@dataclass
class Polygon:
    vertices: List[Vertex]
    _disc: Disc = field(init=False)

    def init_disc(self, disc: Disc) -> None:
        self._disc = weakref.proxy(disc)

    def coordinates(self) -> List[Coordinates]:
        return [self._disc.coordinates[vertex.index] for vertex in self.vertices]


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
            polygons = [
                Polygon([Vertex(int(index)) for index in line.split()])
                for line in index_file.readlines()
            ]
            coordinates = [
                Coordinates(*line.split()) for line in coordinate_file.readlines()
            ]
            disc = Disc(polygons, coordinates)
            for polygon in disc.polygons:
                polygon.init_disc(disc)
                for vertex in polygon.vertices:
                    vertex.init_polygon(polygon)
            return disc


if __name__ == "__main__":
    disc = read_disc("wd-large")
    for coordinates in disc.polygons[0].coordinates():
        print(coordinates)
