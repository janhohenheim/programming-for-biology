#!/usr/bin/env python3
from pathlib import Path
from os.path import join

def _get_code_dir():
    return Path(__file__).parent.absolute()

if __name__ == '__main__':
    with open(join(_get_code_dir(), 'data', 'thompson.txt')) as file:
        lines = file.readlines()
        print(lines[89][:48])
