#!/usr/bin/env python3

def is_permutation_of_palindrome(string: str) -> bool:
    bit_vector = _create_bit_vector(string.replace(' ', '').lower())

    return bit_vector == 0 or _check_exactly_one_bit_set(bit_vector)


def _create_bit_vector(string: str) -> int:
    bit_vector = 0

    for c in string:
        bit_vector = _toggle(bit_vector, ord(c) - 1)

    return bit_vector


def _toggle(bit_vector: int, index: int) -> int:
    if index < 0:
        return bit_vector

    mask = 1 << index

    if (bit_vector & mask) == 0:
        bit_vector |= mask
    else:
        bit_vector &= ~mask

    return bit_vector


def _check_exactly_one_bit_set(bit_vector: int) -> bool:
    return bit_vector & (bit_vector - 1) == 0
