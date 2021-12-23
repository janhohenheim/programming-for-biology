#!/usr/env/bin python3
import numpy.random as rd
import time


def random_list(length):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    l = []
    for i in range(length):
        s = ""
        for j in range(5):
            s += alphabet[rd.randint(0, 24)]
        l.append(s)
    return l


def element_to_index(list_):
    dictionary = {}
    for i, element in enumerate(list_):
        if element not in dictionary:
            dictionary[element] = [i]
        else:
            dictionary[element].append(i)
    return dictionary


if __name__ == "__main__":
    rd.seed(0)
    l1 = random_list(10000)
    l2 = random_list(10000)

    time1 = time.time()
    common = []
    for fruit in l1:
        if fruit in l2:
            if fruit not in common:
                common.append(fruit)
    time2 = time.time()
    print(common)
    print("time spent on list part:", time2 - time1)

    time3 = time.time()
    d1 = element_to_index(l1)
    d2 = element_to_index(l2)

    # time3 = time.time()
    common = []
    for fruit in d1:
        if fruit in d2:
            if fruit not in common:
                common.append(fruit)
    print(common)
    print("time spent on dictionary part:", time.time() - time3)

    print(d1["oodms"])
