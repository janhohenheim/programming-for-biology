#!/usr/bin/env python3
from typing import NamedTuple


class Population(NamedTuple):
    rabbit_count: int
    fox_count: int

    def __add__(self, other):
        return Population(
            rabbit_count=self.rabbit_count + other.rabbit_count,
            fox_count=self.fox_count + other.fox_count,
        )

    def __truediv__(self, other):
        return Population(
            rabbit_count=self.rabbit_count / other,
            fox_count=self.fox_count / other,
        )


def get_population_count(initial_population: Population, days: int) -> Population:
    """
    Return the population after the given number of days.
    """
    return _get_population_count_with_simulation_per_day(
        initial_population, days, simulations_per_day=1
    )


def get_population_count_hourly(
    initial_population: Population, days: int
) -> Population:
    """
    Return the population after the given number of days while simulating every hour.
    """
    return _get_population_count_with_simulation_per_day(
        initial_population, days, simulations_per_day=24
    )


def get_population_count_minutely(
    initial_population: Population, days: int
) -> Population:
    """
    Return the population after the given number of days while simulating every minute.
    """
    return _get_population_count_with_simulation_per_day(
        initial_population, days, simulations_per_day=24 * 60
    )


def _get_population_count_with_simulation_per_day(
    initial_population: Population, days: int, simulations_per_day: int
) -> Population:
    population = initial_population
    for _ in range(days * simulations_per_day):
        population += _get_population_delta(population) / simulations_per_day
    return _round_down(population)


def _get_population_delta(population: Population) -> Population:
    """
    Return the population after one day.
    """
    newborn_rabbit_count = population.rabbit_count * 0.05
    dead_rabbit_count = population.rabbit_count * population.fox_count * 0.0002
    newborn_fox_count = population.rabbit_count * population.fox_count * 0.0001
    dead_fox_count = population.fox_count * 0.1
    return Population(
        rabbit_count=newborn_rabbit_count - dead_rabbit_count,
        fox_count=newborn_fox_count - dead_fox_count,
    )


def _round_down(population: Population):
    return Population(
        rabbit_count=(int)(population.rabbit_count),
        fox_count=(int)(population.fox_count),
    )


if __name__ == "__main__":
    print("Simulating daily:")
    initial_population = Population(rabbit_count=1000, fox_count=100)
    days = 100
    final_population = get_population_count(initial_population, days)
    print(
        f"After {days} days, the population went from {initial_population} to {final_population}"
    )

    days = 1542
    final_population = get_population_count(initial_population, days)
    print(
        f"After {days} days, the population went from {initial_population} to {final_population}"
    )

    print("Simulating hourly:")
    days = 200
    final_population = get_population_count_hourly(initial_population, days)
    print(
        f"After {days} days, the population went from {initial_population} to {final_population}"
    )

    print("Simulating minutely:")
    days = 200
    final_population = get_population_count_minutely(initial_population, days)
    print(
        f"After {days} days, the population went from {initial_population} to {final_population}"
    )
