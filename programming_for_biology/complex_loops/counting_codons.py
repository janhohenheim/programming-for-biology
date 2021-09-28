#!/usr/bin/env python3


def generate_codons():
    bases = ["A", "T", "C", "G"]
    for first_base in bases:
        for second_base in bases:
            for third_base in bases:
                yield first_base + second_base + third_base


def count_codons_up_to(combination_count):
    codons = generate_codons()
    indices = range(1, combination_count + 1)
    return zip(indices, codons)


def count_filtered_codons_up_to(combination_count, filter_function):
    codons = generate_codons()
    indices = range(1, combination_count + 1)
    return zip(indices, filter(filter_function, codons))


def filter_codon(codon):
    return (codon[0] == codon[1] or codon[1] == codon[2]) and codon[0] != codon[2]


if __name__ == "__main__":
    for i, codon in count_codons_up_to(45):
        print(i, codon)

    filtered_codons = count_filtered_codons_up_to(19, filter_codon)
    for i, codon in filtered_codons:
        print(i, codon)
