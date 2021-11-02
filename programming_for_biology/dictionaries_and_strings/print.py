#!/usr/bin/env python3
from numpy import pi

if __name__ == '__main__':
    p = int(10**7 * pi)
    print(f'{p:011} is an integer')
    print(f'{pi:015.10} is a float')
    print(f'{pi:019.9e} is a float in exp notation')
    