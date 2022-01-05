#!/usr/bin/env python3
from Bio import ExPASy, SeqIO
from pathlib import Path
from os.path import join


def get_code_dir():
    return Path(__file__).parent.absolute()


def fetch_genbank(sid):
    # fetches a genbank file (sid = sequence ID) from Uniprot
    try:
        handle = ExPASy.get_sprot_raw(sid)
        seq = SeqIO.read(handle, "swiss")
        path = join(get_code_dir(), "data", f"{sid}.genbank")
        SeqIO.write(seq, path, "genbank")
        print(sid, "sequence length", len(seq))
    except Exception:
        print(sid, "not found")


def read_genbank(fname):
    # extracts the organism name and the sequence
    # from a local genbank file
    path = join(get_code_dir(), "data", fname)
    f = open(path)
    for p in SeqIO.parse(f, "genbank"):
        break
    f.close()
    return p.annotations["organism"], str(p.seq)


if __name__ == "__main__":
    # fetch a genbank file for a specific sequence ID
    # and read in the organism and the sequence.
    sequences = ["P00846", "Q95A26", "Q9T9W0", "Q2I3G9", "Q9TA24"]
    for sequence in sequences:
        fetch_genbank(sequence)
        organism, seq = read_genbank(sequence + ".genbank")
        print(sequence, organism, seq)
