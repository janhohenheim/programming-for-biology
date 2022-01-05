#!/usr/bin/env python3

import math


def get_longest_shared_sequence(a: str, b: str) -> str:
    shared_sequences = []
    for window_size in range(1, len(a) + 1):
        for window_start in range(len(a)):
            window_end = window_start + window_size
            window = a[window_start:window_end]
            if window in b:
                shared_sequences.append(window)
    return max(shared_sequences, key=len)


if __name__ == "__main__":
    a = "MNENLFASFIAPTILGLPAAVLIILFPPLLIPTSKYLINNRLITTQQWLIKLTSKQMMTMHNTKGRTWSLMLVSLIIFIATTNLLGLLPHSFTPTTQLSMNLAMAIPLWAGTVIMGFRSKIKNALAHFLPQGTPTPLIPMLVIIETISLLIQPMALAVRLTANITAGHLLMHLIGSATLAMSTINLPSTLIIFTILILLTILEIAVALIQAYVFTLLVSLYLHDNT"
    b = "MMTNLFSVFDPSTTILNLSLNWLSTFLGLLLIPFSFWLLPNRFQVVWNNILLTLHKEFKTLLGPSGHNGSTLMFISLFSLIMFNNFLGLFPYIFTSTSHLTLTLALAFPLWLSFMLYGWINHTQHMFAHLVPQGTPPVLMPFMVCIETISNVIRPGTLAVRLTANMIAGHLLLTLLGNTGPMTTNYIILSLILTTQIALLVLESAVAIIQSYVFAVLSTLYSSEVN"
    print(get_longest_shared_sequence(a, b))
