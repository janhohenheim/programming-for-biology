#!/usr/bin/env python3
from pathlib import Path
from os.path import join

def _get_code_dir():
    return Path(__file__).parent.absolute()

def read_riddle():
    with open(join(_get_code_dir(), 'data', 'riddle.txt')) as file:
        lines = file.readlines()
        return "".join(lines)

if __name__ == '__main__':
    riddle = read_riddle()
    begin = "*****"
    end = "#####"
    pivot_begin = riddle.find(begin)
    pivot_end = riddle.find(end)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    word = "".join([letter for letter in riddle[pivot_begin:pivot_end] if letter in alphabet])
    print(word)