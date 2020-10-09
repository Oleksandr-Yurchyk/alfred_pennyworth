from typing import List, Dict
import string
import random

Alphabet = List[Dict[str, int]]


def generate_alphabet() -> Alphabet:
    """
    Generate list of dicts.
    Where each dict contain 1 pair of key/value
    key - letter from alphabet
    value - random int value from 0 to 100
    """
    alpha = []
    for letter in string.ascii_lowercase:
        alpha.append(dict([(letter, random.randint(0, 100))]))
    return alpha


def sort_alphabet(data: Alphabet) -> Alphabet:
    """
    Sort incoming alphabet by int values.
    """
    list_of_tuples = []
    list_of_dict = []
    for i in data:
        list_of_tuples += i.items()
    list_of_tuples.sort(key=lambda x: x[1])
    for i in list_of_tuples:
        list_of_dict.append(dict([(i[0], i[1])]))
    return list_of_dict
