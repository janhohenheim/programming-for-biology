#!/usr/bin/env python3

def filter_string(s):
    return "".join([letter for i, letter in enumerate(s) if i % 4 == 0 or (i-1) % 4 == 0])

if __name__ == '__main__':
    s = 'ztvnenejsncejajdncalkjalymmxndjfbfbvsjdlfjbbaldkjfnlaqeqwqwplnnnel'
    print(filter_string(s))