#!/usr/bin/env python3


def generate_codons():
    bases = ["A", "T", "C", "G"]
    for first_base in bases:
        for second_base in bases:
            for third_base in bases:
                yield first_base + second_base + third_base


def count_codons_up_to(combination_count):
    codons = generate_codons()
    return zip(range(1, combination_count + 1), codons)


if __name__ == "__main__":
    for i, codon in count_codons_up_to(45):
        print(i, codon)
