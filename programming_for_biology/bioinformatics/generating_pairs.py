#!/usr/bin/env python3


def generate_unique_pairs(list_):
    pairs = set()
    for element in list_:
        for other_element in list_:
            if element != other_element and (other_element, element) not in pairs:
                pairs.add((element, other_element))
    return [list(pair) for pair in pairs]


if __name__ == "__main__":
    objects = ["ball", "clock", "glass", "table"]
    unique_pairs = generate_unique_pairs(objects)
    print(unique_pairs)
