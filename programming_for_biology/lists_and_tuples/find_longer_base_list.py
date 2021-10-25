#!/usr/bin/env python3

if __name__ == '__main__':
    letters = ['o', 'e', 'o', 'y', 'c', 'q', 'o', 'p', 'q', 'v', 'x', 'h', 'd', 'g', 'g', 'w', 'x', 'v', 'w', 'd', 'j', 'b', 'b', 'p', 'f', 'f', 'i', 'y', 'v', 'j', 'd', 'z', 'b', 'u', 'y', 'y', 'q', 'y', 'i', 'v', 'y', 'r', 'l', 'l', 'e', 'i', 'g', 's', 'g', 'x', 'd', 'g', 'm', 'z', 'y', 'j', 'd', 'n', 'p', 'z', 'p', 'r', 'i', 'v', 'h', 'l', 'j', 'h', 'k', 'r', 's', 'n', 'e', 'g', 'i', 'q', 'v', 'e', 'r', 'y']
    possible_dna_bases = ['a', 'c', 'g', 't']
    possible_rna_bases = ['a', 'c', 'g', 'u']
    dna_bases = [l for l in letters if l in possible_dna_bases]
    rna_bases = [l for l in letters if l in possible_rna_bases]
    longer_list = dna_bases if len(dna_bases) > len(rna_bases) else rna_bases
    print(longer_list)