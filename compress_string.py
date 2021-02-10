def compress_string(text):
    """
    Write a function which will "compress" input string.
    Instead of repeating a char there should be just number of repetitions.
    >>> compress_string('aaabbbbcddd')
    'a3b4cd3'
    >>> compress_string('abcdefgh')
    'abcdefgh'
    >>> compress_string('aaaaabaaaaa')
    'a5ba5'
    >>> compress_string('aaaaaaaaaab')
    'a10b'
    >>> compress_string('')
    ''
    """
    result = ''
    i, counter = 1, 1
    if len(text) == 0:
        result = ''
        return result
    while True:
        if i == len(text):
            if counter > 1:
                result += text[i-1] + str(counter)
            else:
                result += text[i-1]
            break
        if text[i] != text[i - 1]:
            if counter > 1:
                result += text[i - 1] + str(counter)
            else:
                result += text[i - 1]
            counter = 1
        else:
            counter += 1
        i += 1
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
