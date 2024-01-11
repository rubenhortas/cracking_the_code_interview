def get_compressed_string(string: str) -> str:
    # Time complexity: O(n)
    # Auxiliary space: O(1)

    # Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
    # Avoid using the + and += operators to accumulate a string within a loop.
    # In some conditions, accumulating a string with addition can lead to quadratic rather than linear running time.
    # Although common accumulations of this sort may be optimized on CPython, that is an implementation detail.
    # The conditions under which an optimization applies are not easy to predict and may change.Instead,
    # add each substring to a list and ''.join the list after the loop terminates, or write each substring
    # to an io.StringIO buffer.These techniques consistently have amortized-linear run-time complexity.
    compressed_string_tmp = []
    current_char = string[0]
    current_char_count = 1

    for i in range(0, len(string) - 1):
        next_char = string[i + 1]

        if current_char == next_char:
            current_char_count = current_char_count + 1
        else:
            compressed_string_tmp.append(f"{current_char}{current_char_count}")
            current_char = next_char
            current_char_count = 1

    compressed_string_tmp.append(f"{current_char}{current_char_count}")
    compressed_string = ''.join(compressed_string_tmp)

    if len(compressed_string) < len(string):
        return compressed_string
    else:
        return string
