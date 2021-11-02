#!/usr/bin/env python3

def get_codons_to_aminos():
    cdn = {}
    cdn["ttt"] = cdn["ttc"] = "F phenylalanine"
    cdn["tta"] = cdn["ttg"] = "L leucine"
    cdn["tct"] = cdn["tcc"] = cdn["tca"] = cdn["tcg"] = "S serine"
    cdn["tat"] = cdn["tac"] = "Y tyrosine"
    cdn["taa"] = cdn["tag"] = "* stop"
    cdn["tgt"] = cdn["tgc"] = "C cysteine"
    cdn["tga"] = "* stop"
    cdn["tgg"] = "W tryptophan"
    cdn["ctt"] = cdn["ctc"] = cdn["cta"] = cdn["ctg"] = "L leucine"
    cdn["cct"] = cdn["ccc"] = cdn["cca"] = cdn["ccg"] = "P proline"
    cdn["cat"] = cdn["cac"] = "H histidine"
    cdn["caa"] = cdn["cag"] = "Q glutamine"
    cdn["cgt"] = cdn["cgc"] = cdn["cga"] = cdn["cgg"] = "R arginine"
    cdn["att"] = cdn["atc"] = cdn["ata"] = "I isoleucine"
    cdn["atg"] = "M methionine"
    cdn["act"] = cdn["acc"] = cdn["aca"] = cdn["acg"] = "T threonine"
    cdn["aat"] = cdn["aac"] = "N asparagine"
    cdn["aaa"] = cdn["aag"] = "K lysine"
    cdn["agt"] = cdn["agc"] = "S serine"
    cdn["aga"] = cdn["agg"] = "R arginine"
    cdn["gtt"] = cdn["gtc"] = cdn["gta"] = cdn["gtg"] = "V valine"
    cdn["gct"] = cdn["gcc"] = cdn["gca"] = cdn["gcg"] = "A alanine"
    cdn["gat"] = cdn["gac"] = "D aspartic acid"
    cdn["gaa"] = cdn["gag"] = "E glutamic acid"
    cdn["ggt"] = cdn["ggc"] = cdn["gga"] = cdn["ggg"] = "G glycine"
    return cdn

def get_aminos_to_codons():
    cdn = get_codons_to_aminos()
    cdn_rev = {amino:[] for amino in cdn.values()}
    for codon, amino in cdn.items():
        cdn_rev[amino].append(codon)
    return cdn_rev

if __name__ == "__main__":
    cdn = get_codons_to_aminos()
    sequence = "atgagtaaaggagaagaacttttcactggagttgttccaattcttgttgaattagatggt"
    codons = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
    amino_acids = [cdn[codon] for codon in codons]
    amino_acid_letters = [amino_acid.split(" ")[0] for amino_acid in amino_acids]
    amino_acid_sequence = "".join(amino_acid_letters)
    print(amino_acid_sequence)

    cdn_rev = get_aminos_to_codons()
    serine_codons = sorted(cdn_rev["S serine"])
    print(serine_codons[4])

