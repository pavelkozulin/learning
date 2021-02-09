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
    b = ''
    i, j = 1, 1
    if len(text) == 0:
        b = ''
    else:
        while True:
            #print('i, j', i, j)
            if i == len(text):
                if j > 1:
                    b += text[i-1] + str(j)
                else:
                    b += text[i-1]
                #print('max_len')
                break
            if text[i] != text[i - 1]:
                if j > 1:
                    b += text[i - 1] + str(j)
                else:
                    b += text[i - 1]    
                j = 1
                #print('ab', b)
            else:
                j += 1
            i += 1
    return b

if __name__ == '__main__':
    import doctest
    doctest.testmod()
