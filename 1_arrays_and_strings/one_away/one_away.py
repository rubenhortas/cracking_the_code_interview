#!/usr/bin/env python3

"""
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
"""


def one_away(str1: str, str2: str) -> bool:
    if len(str2) == len(str1):
        return _hasOnlyOneReplaced(str1, str2)
    elif len(str2) == len(str1) + 1:
        return _hasOnlyOneInseredtOrRemoved(str1, str2)
    elif len(str2) == len(str1) - 1:
        return _hasOnlyOneInseredtOrRemoved(str2, str1)
    else:
        return False


def _hasOnlyOneReplaced(str1: str, str2: str) -> bool:
    found_difference = False

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if found_difference:
                return False
            else:
                found_difference = True

    return True


def _hasOnlyOneInseredtOrRemoved(str1: str, str2: str) -> bool:
    index1 = 0
    index2 = 0

    while index2 < len(str2) and index1 < len(str1):
        if str1[index1] != str2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1

    return True
