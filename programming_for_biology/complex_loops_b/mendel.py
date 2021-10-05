#!/usr/bin/env python3

from enum import Enum, auto
from typing import Dict, NamedTuple, List, Tuple, TypedDict
import numpy.random as rnd


class Generation(NamedTuple):
    first: int
    second: int
    expected_proportion: float

    def total(self):
        return self.first + self.second


class ClosestMeasurement(Enum):
    MENDEL = auto()
    SIMULATION = auto()
    BOTH = auto()


def get_closest_measurement(
    mendel_values: Generation, simulation_values: Generation
) -> Dict[ClosestMeasurement, int]:
    expected_first = mendel_values.expected_proportion * mendel_values.total()
    mendel_error = abs(expected_first - mendel_values.first)
    simulation_error = abs(expected_first - simulation_values.first)
    if mendel_error < simulation_error:
        return ClosestMeasurement.MENDEL
    elif simulation_error < mendel_error:
        return ClosestMeasurement.SIMULATION
    else:
        return ClosestMeasurement.BOTH


def simulate_generation(mendel_generation) -> Generation:
    total = mendel_generation.total()
    expected_proportion = mendel_generation.expected_proportion
    first = rnd.binomial(total, expected_proportion)
    second = total - first
    return Generation(first, second, expected_proportion)


def get_generation_pair(mendel_generation: Generation) -> Tuple[Generation, Generation]:
    return mendel_generation, simulate_generation(mendel_generation)


def run_simulation_for_generation(
    mendel_values: Generation, rounds: int
) -> Dict[ClosestMeasurement, int]:
    generations = [get_generation_pair(mendel_values) for _ in range(rounds)]
    closest_measurements = [
        get_closest_measurement(mendel_generation, simulated_generation)
        for mendel_generation, simulated_generation in generations
    ]
    return {
        closest_measurement: closest_measurements.count(closest_measurement)
        for closest_measurement in closest_measurements
    }


def run_simulation(
    mendel_values: List[Generation], rounds: int
) -> List[Dict[ClosestMeasurement, int]]:
    return [
        run_simulation_for_generation(mendel_values, rounds)
        for mendel_values in mendel_values
    ]


if __name__ == "__main__":
    mendel = [
        Generation(5474, 1850, 3 / 4),
        Generation(6022, 2001, 3 / 4),
        Generation(705, 224, 3 / 4),
        Generation(882, 299, 3 / 4),
        Generation(428, 152, 3 / 4),
        Generation(651, 207, 3 / 4),
        Generation(787, 277, 3 / 4),
        Generation(372, 193, 2 / 3),
        Generation(353, 166, 2 / 3),
        Generation(64, 36, 2 / 3),
        Generation(71, 29, 2 / 3),
        Generation(60, 40, 2 / 3),
        Generation(67, 33, 2 / 3),
        Generation(72, 28, 2 / 3),
        Generation(65, 35, 2 / 3),
    ]
    simulated_rounds = 1_000
    results = run_simulation(mendel, simulated_rounds)
    print([result.get(ClosestMeasurement.MENDEL, 0) for result in results])
    print([result.get(ClosestMeasurement.SIMULATION, 0) for result in results])
