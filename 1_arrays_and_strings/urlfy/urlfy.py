def get_url(string: list, true_length: int) -> list:
    # Time complexity: O(n)
    # Auxiliary space: O(1)
    spaces = 0

    for i in reversed(range(true_length)):
        if string[i] == ' ':
            spaces = spaces + 1

    index = (true_length + (2 * spaces)) - 1

    for i in reversed(range(true_length)):
        if string[i] != ' ':
            string[index] = string[i]
            index = index - 1
        else:
            string[index] = '0'
            index = index - 1

            string[index] = '2'
            index = index - 1

            string[index] = '%'
            index = index - 1

    return string
