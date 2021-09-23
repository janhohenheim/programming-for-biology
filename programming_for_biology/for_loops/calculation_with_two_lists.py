#!/usr/bin/env python3
def get_shifted_product(first_list: list, second_list: list) -> list:
    """
    Returns a list of the product of each element in the first list
    with each element in the second list shifted by one index.
    """
    shifted_second_list = second_list[1:]
    return [a * b for a, b in zip(first_list, shifted_second_list)]


if __name__ == "__main__":
    first_list = [7, 3, 2, 5, 1, 4, 4, 6, 2, 9, 1, 6, 3, 2, 6, 5, 5]
    second_list = [8, 9, 8, 9, 6, 4, 5, 5, 8, 2, 4, 3, 1, 6, 5, 6, 5]
    shifted_product = get_shifted_product(first_list, second_list)
    print(sum(shifted_product))
