import string
def words_to_marks(word):
    """
    >>> words_to_marks('attitude')
    100
    >>> words_to_marks('friends')
    75
    >>> words_to_marks('family')
    66
    >>> words_to_marks('selfness')
    99
    >>> words_to_marks('knowledge')
    96
    """

    letter_number_dict = dict(zip(string.ascii_lowercase, [i for i in range(1, 27)]))

    return sum((letter_number_dict[i] for i in word))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
