# Pythonic way using itertools

import itertools


def get_compressed_string(string: str) -> str:
    groups = itertools.groupby(string)  # https://docs.python.org/3/library/itertools.html#itertools.groupby
    compressed = ''.join(f'{k}{len(list(g))}' for k, g in groups)

    if len(compressed) < len(string):
        return compressed
    else:
        return string
