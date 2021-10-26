#!/usr/bin/env python3
from itertools import groupby


def generate_codons():
    bases = ["A", "T", "C", "G"]
    for first_base in bases:
        for second_base in bases:
            for third_base in bases:
                yield first_base + second_base + third_base


def get_anticodon(codon):
    return [get_complementary_base(base) for base in codon]


def get_complementary_base(base):
    base_pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return base_pairs[base]


def get_gamov_diamond(codon):
    anticodon = get_anticodon(codon)
    gamov_diamond = [codon[0], codon[1], anticodon[1], anticodon[2]]
    gamov_diamond = sorted(gamov_diamond)
    return "".join(gamov_diamond)


if __name__ == "__main__":
    codons = generate_codons()
    gamov_and_codon = [(get_gamov_diamond(codon), codon) for codon in codons]
    gamov_and_codon = sorted(gamov_and_codon)
    gamov_to_codon = {
        gamov: [v[1] for v in valuesiter]
        for gamov, valuesiter in groupby(gamov_and_codon, lambda x: x[0])
    }
    codons = sorted(list(gamov_to_codon.values()))
    print(codons)
    print(codons[5][0])
