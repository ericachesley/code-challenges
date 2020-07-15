"""Write a function that compresses a string.

Repeated characters should be compressed to one character and the number of
times it repeats:

>>> compress('aabbaabb')
'a2b2a2b2'

If a character appears once, it should not be followed by a number:

>>> compress('abc')
'abc'

The function should handle letters, whitespace, and punctuation:

>>> compress('Hello, world! Cows go moooo...')
'Hel2o, world! Cows go mo4.3'
"""


def compress(string):
    """Return a compressed version of the given string."""
    count = 1
    new = string[0]
    for char in string[1:]:
        if char != new[-1]:
            if count > 1:
                new += str(count)
                count = 1
            new += char
        else:
            count += 1
    if count > 1:
        new += str(count)
    return new


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
