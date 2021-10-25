#!/usr/bin/env python3
from pathlib import Path
from os.path import join

def _get_code_dir():
    return Path(__file__).parent.absolute()

if __name__ == '__main__':
    with open(join(_get_code_dir(), 'data', 'crick.txt')) as input:
        with open(join(_get_code_dir(), 'data', 'crick_copy.txt'), 'w') as output:
            lines = [line.strip() for line in input.readlines()]
            text = ' '.join(lines)            
            output.write(text)
            print(text)
