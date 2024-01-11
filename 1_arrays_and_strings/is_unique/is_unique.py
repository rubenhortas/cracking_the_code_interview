def is_unique(string: str) -> bool:
    # Time complexity: O(n)
    # Auxiliary space: O(1)

    # Let's assume that is an ASCII string.
    # ASCII has just 128 code points, of which only 95 are printable characters.
    # UTF-8 is capable of encoding all 1,112,064[a] valid Unicode code points.
    # If it were a UTF-8 string, we would need to use more memory.
    chars = [False] * 128

    for i in range(len(string)):
        if chars[ord(string[i])]:
            return False

        chars[ord(string[i])] = True

    return True
