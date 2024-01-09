def is_unique(string: str) -> bool:
    # Time complexity: O(n^2)
    # Auxiliary space: O(1)

    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False

    return True
