#!/usr/bin/env python3
from pathlib import Path
from os.path import join

def _get_code_dir():
    return Path(__file__).parent.absolute()

if __name__ == '__main__':
    with open(join(_get_code_dir(), 'data', 'darwin.txt')) as file:
        lines = file.readlines()
        lines_of_words = [line.split() for line in lines]
        third_words = [words[2] for words in lines_of_words]
        lengths = [len(word) for word in third_words]
        average_length = sum(lengths) / len(lengths)
        print(average_length)
