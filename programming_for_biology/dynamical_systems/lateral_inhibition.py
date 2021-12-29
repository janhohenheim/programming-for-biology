#!/usr/env/bin python3
from dataclasses import dataclass
from typing import List
import numpy as np
import logging


@dataclass(frozen=True)
class Cell:
    notch: float
    delta: float

    def __add__(self, other):
        return Cell(
            notch=self.notch + other.notch,
            delta=self.delta + other.delta,
        )

    def __mul__(self, scalar: float):
        return Cell(
            notch=self.notch * scalar,
            delta=self.delta * scalar,
        )

    def __truediv__(self, scalar: float):
        return Cell(
            notch=self.notch / scalar,
            delta=self.delta / scalar,
        )

    def __str__(self):
        return f"{self.notch} notch, {self.delta} delta"


@dataclass(frozen=True)
class LateralInhibitionSystem:
    a: float
    b: float
    k: float
    h: float
    time_step: float = 0.2

    def _dt_notch(self, proteins: List[Cell], index) -> float:
        notch = proteins[index].notch
        neighbors = [
            proteins[index - 1] if index > 0 else None,
            proteins[index + 1] if index < len(proteins) - 1 else None,
        ]
        mean_neighbor_delta = np.mean([p.delta for p in neighbors if p is not None])
        d = mean_neighbor_delta ** self.k
        return d / (self.a + d) - notch

    def _dt_delta(self, proteins: List[Cell], index) -> float:
        notch = proteins[index].notch
        delta = proteins[index].delta
        return 1 / (1 + self.b * notch ** self.h) - delta

    def _dt_proteins(self, proteins: List[Cell]) -> List[Cell]:
        return np.array(
            [
                Cell(
                    notch=self._dt_notch(proteins, i),
                    delta=self._dt_delta(proteins, i),
                )
                for i in range(len(proteins))
            ]
        )

    def after_time(self, proteins: List[Cell], delta_time) -> List[Cell]:
        updated_proteins = np.array(proteins)
        for _ in np.arange(0, delta_time, self.time_step):
            dt_proteins = self._dt_proteins(updated_proteins)
            updated_proteins += dt_proteins * self.time_step
            print(updated_proteins)
            exit()
        return updated_proteins


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    lateral_inhibition_system = LateralInhibitionSystem(a=0.01, b=100, k=2, h=2)
    initial_cells = [Cell(notch=1, delta=0.99), Cell(notch=1, delta=1)]
    delta_time = 50
    final_cells = lateral_inhibition_system.after_time(initial_cells, delta_time)
    print(f"After {delta_time} time units, the population went:")
    for i, (initial, final) in enumerate(zip(initial_cells, final_cells)):
        print(f"Cell {i}: {initial} -> {final}")
