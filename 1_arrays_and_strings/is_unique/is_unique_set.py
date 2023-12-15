#!/usr/bin/env python3

# Pythonic way using set

def is_unique(string: str) -> bool:
    return len(string) == len(set(string))
