# Pythonic way using counter

from collections import Counter


def is_unique(string: str) -> bool:
    counter = Counter(string)

    return all(counter[char] <= 1 for char in counter)
