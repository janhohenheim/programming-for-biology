#!/usr/bin/env python3
import numpy as np


def dt_x(c, x):
    return c * x


def simulate_prey_using_euler_method(c, x0, t, delta_t):
    x = x0
    for _ in np.arange(0, t, delta_t):
        x += dt_x(c, x) * delta_t
    return x


def simulate_prey_using_midpoint_method(c, x0, t, delta_t):
    x = x0
    for _ in np.arange(0, t, delta_t):
        dx_dt0 = c * x
        x05 = x + 0.5 * dx_dt0 * delta_t
        dx_dt05 = c * x05
        x += dx_dt05 * delta_t
    return x


def simulate_prey_using_analytical_method(c, x0, t):
    return x0 * np.exp(c * t)


def get_prey_euler_simulation_error(c, x0, t, delta_t):
    return simulate_prey_using_euler_method(
        c, x0, t, delta_t
    ) - simulate_prey_using_analytical_method(c, x0, t)


def get_prey_midpoint_simulation_error(c, x0, t, delta_t):
    return simulate_prey_using_midpoint_method(
        c, x0, t, delta_t
    ) - simulate_prey_using_analytical_method(c, x0, t)


def print_error(delta_t):
    c = 0.03
    x0 = 1000.0
    t = 20.0

    euler_error = get_prey_euler_simulation_error(c, x0, t, delta_t)
    print(f"Euler error with delta t = {delta_t}: {euler_error}")
    midpoint_error = get_prey_midpoint_simulation_error(c, x0, t, delta_t)
    print(f"Midpoint error with delta t = {delta_t}: {midpoint_error}")


if __name__ == "__main__":
    print_error(0.05)
    print_error(0.1)
    print_error(0.2)
