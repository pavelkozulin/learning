def decompress_string(text):
    """
    Write a inverse function.

    >>> decompress_string('')
    ''
    >>> decompress_string('a10b')
    'aaaaaaaaaab'
    >>> decompress_string('a5ba5')
    'aaaaabaaaaa'
    >>> decompress_string('a3b4cd3')
    'aaabbbbcddd'
    """

    if text == '':
        b = ''
    else:
        b = ''
        i = 1
        while True:
            print('i', i)
            print('text[i]', text[i])
            if text[i].isdigit():
                b += text[i - 1] * int(text[i])
                print('DIGIT, b', b)
            elif i == len(text):
                b += text[i - 1] * text[i]
                print('lenmax')
                break
            else:
                b += text[i]
                print('else, b', b)
            i += 1

    return b


if __name__ == '__main__':
    import doctest
    doctest.testmod()
