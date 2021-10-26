#!/usr/bin/env python3
from pathlib import Path
from os.path import join
import csv


def _get_code_dir():
    return Path(__file__).parent.absolute()


def read_csv(filename):
    path = get_filepath(filename)
    with open(path, "r") as f:
        reader = csv.reader(f)
        labels = ["index"] + next(reader)[1:]
        return {row[0]: dict(zip(labels, [i] + row[1:])) for i, row in enumerate(reader)}

def get_filepath(filename):
    return join(_get_code_dir(), "data", filename)


if __name__ == "__main__":
    brain = read_csv("human_brain_proteins.csv")
    plasma = read_csv("human_plasma_proteins.csv")
    print("Number of brain proteins:", len(brain))
    print("Number of plasma proteins:", len(plasma))

    brain_only = brain.keys() - plasma.keys()
    plasma_only = plasma.keys() - brain.keys()
    brain_and_plasma = brain.keys() & plasma.keys()
    print("Number of brain proteins only:", len(brain_only))
    print("Number of plasma proteins only:", len(plasma_only))
    print("Number of proteins in both:", len(brain_and_plasma))

    brain_protein = sorted(list(brain_only))[520]
    print("brain_only[520]:", brain_protein)
    plasma_protein = sorted(list(plasma_only))[520]
    print("plasma_only[520]:", plasma_protein)
    brain_and_plasma_protein = sorted(list(brain_and_plasma))[520]
    print("brain_and_plasma[520]:", brain_and_plasma_protein)