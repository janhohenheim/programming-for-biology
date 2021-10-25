#!/usr/bin/env python3

if __name__ == '__main__':
    string = 'dfkfje*jfdn*pwndnv*sfkjadjbvbjbajbfkaj*nkd*nvndlanakndndhnfajnja*lsdkjf*cevgfjh**nfe*en*m\r\n'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = [letter for letter in string if letter in alphabet]
    letters = ''.join(letters)
    print(len(letters))
    