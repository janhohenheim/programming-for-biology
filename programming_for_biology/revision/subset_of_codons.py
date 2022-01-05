#!/usr/bin/env python3

from programming_for_biology.complex_loops.counting_codons import generate_codons


def count_same_bases(codon):
    if codon[0] == codon[1] and codon[1] == codon[2]:
        return 3
    elif codon[0] == codon[1] or codon[1] == codon[2] or codon[0] == codon[2]:
        return 2
    else:
        return 1


def filter_codons_with_same_bases(codons, base_count):
    return [codon for codon in codons if count_same_bases(codon) == base_count]


if __name__ == "__main__":
    codons = generate_codons()
    filtered_codons = sorted(filter_codons_with_same_bases(codons, 2))
    print(filtered_codons)
