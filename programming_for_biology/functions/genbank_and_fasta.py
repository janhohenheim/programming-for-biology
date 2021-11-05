#!/usr/bin/env python3
import re

_genbank_locus_re = r"$LOCUS\s+([\w\d_]+).*^"
_genbank_recname_re = r"$DEFINITION\s+RecName: ([\w\d_ =]+)^"
_genbank_sequence_begin_re = r"$ORIGIN\s+RecName: (\s+\d+[\w\d_]
def convert_genbank_entry_to_fasta(genbank: str, sequence_id: str) -> str:
    

if __name__ == "__main__":