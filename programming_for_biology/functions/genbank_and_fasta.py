#!/usr/bin/env python3
import re
from typing import NamedTuple, List
from pathlib import Path
from os.path import join

class PeptideRecord(NamedTuple):
    locus: str
    name: str
    sequence: str
    
    def _split_amino_lines_by_groups(self, sequence: str, group_size, groups_per_line) -> List[List[str]]:
        amino_groups = [sequence[i:i+group_size] for i in range(0, len(sequence), group_size)]
        return [amino_groups[i:i+groups_per_line] for i in range(0, len(amino_groups), groups_per_line)]


    def as_genbank(self) -> str:
        group_size = 10
        groups_per_line = 6
        aminos_per_line = groups_per_line * group_size
        amino_lines = self._split_amino_lines_by_groups(self.sequence, group_size, groups_per_line)
        amino_lines = [[amino.lower() for amino in line] for line in amino_lines]
        print(amino_lines)
        amino_lines = [[f"{(aminos_per_line * i + 1): 9d}"] + line for i, line in enumerate(amino_lines)]
        amino_lines_str = "\n".join([" ".join(line) for line in amino_lines])
        return f"LOCUS {self.locus}\nDEFINITION RecName: {self.name}\nORIGIN\n{amino_lines_str}\n//"

    
    def as_fasta(self) -> str:
        amino_lines = self._split_amino_lines_by_groups(self.sequence, 60, 1)
        amino_lines = [[amino.upper() for amino in line] for line in amino_lines]
        amino_lines_str = "\n".join([" ".join(line) for line in amino_lines])
        return f">{self.locus} RecName: {self.name};\n{amino_lines_str}"


_genbank_locus_re = r"^LOCUS\s+([\w\d_]+).*$"
_genbank_recname_re = r"^^DEFINITION\s+RecName: ([\w\d_ =]+).*$"
_genbank_sequence_begin_re = r"^ORIGIN$"
_genbank_sequence_line_re = r"^\s+ \d+ ([\w ]+)$"
_genbank_sequence_end_re = r"//"

_fasta_header_re = r"^>(:?\w+\|[\d\w]+\|)?([\d\w_]+)\s+(:?RecName: )?(.*)$"

def parse_genbank(lines: List[str]) -> dict:
    records = {}
    locus = None
    recname = None
    sequence = None
    in_sequence = False
    for line in lines:
        if re.match(_genbank_locus_re, line):
            locus = re.search(_genbank_locus_re, line).group(1)
        elif re.match(_genbank_recname_re, line):
            recname = re.search(_genbank_recname_re, line).group(1)
        elif re.match(_genbank_sequence_begin_re, line):
            in_sequence = True
        elif in_sequence and re.match(_genbank_sequence_line_re, line):
            if sequence is None:
                sequence = ""
            sequence_fragment = re.search(_genbank_sequence_line_re, line).group(1).replace(" ", "").upper()
            sequence += sequence_fragment
        elif in_sequence and re.match(_genbank_sequence_end_re, line):
            in_sequence = False
            if locus is None or recname is None or sequence is None:
                raise ValueError(
                    f"Invalid genbank file: locus {locus}, recname {recname}, sequence {sequence}"
                )
            records[locus] = PeptideRecord(locus, recname, sequence)
            locus = None
            recname = None
            sequence = None
    return records

def parse_fasta(lines: List[str]) -> dict:
    records = {}
    locus = None
    recname = None
    sequence = None
    for line in lines:
        if re.match(_fasta_header_re, line):
            match = re.search(_fasta_header_re, line)
            locus = match.group(2)
            recname = match.group(4)
            if sequence is not None:
                records[locus] = PeptideRecord(locus, recname, sequence)
                sequence = None
        else:
            if sequence is None:
                sequence = ""
            sequence += line.strip().upper()
    if sequence is not None:
        records[locus] = PeptideRecord(locus, recname, sequence)
    return records
                



def _get_code_dir() -> str:
    return Path(__file__).parent.absolute()

def read_genbank(id: str) -> dict:
    with open(join(_get_code_dir(), "data", f"{id}.genbank.txt")) as file:
        lines = file.readlines()
        return parse_genbank(lines)
            
def read_fasta(id: str) -> dict:
    with open(join(_get_code_dir(), "data", f"{id}.fasta.txt")) as file:
        lines = file.readlines()
        return parse_fasta(lines)

def write_genbank(id: str, records: dict):
    with open(join(_get_code_dir(), "data", f"{id}.genbank.txt"), "w") as file:
        for record in records.values():
            file.write(record.as_genbank())
            file.write("\n")

def write_fasta(id: str, records: dict):
    with open(join(_get_code_dir(), "data", f"{id}.fasta.txt"), "w") as file:
        for record in records.values():
            file.write(record.as_fasta())
            file.write("\n")



if __name__ == "__main__":
    genbank_records = read_genbank("P42677")
    write_fasta("P42677", genbank_records)
    print("GenBank")
    print("-------")
    print("Read the following GenBank records:")
    for record in genbank_records.values():
        print(record.as_genbank())
    print("Wrote the following records:")
    for record in genbank_records.values():
        print(record.as_fasta())

    fasta_records = read_fasta("Q9NSA3")
    write_genbank("Q9NSA3", fasta_records)

    print("Fasta")
    print("-----")
    print("Read the following Fasta records:")
    for record in fasta_records.values():
        print(record.as_fasta())
    print("Wrote the following records:")
    for record in fasta_records.values():
        print(record.as_genbank())


