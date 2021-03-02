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

    result = []
    last_letter = ''
    buffer = []

    for i in text:
        #print('i = ', i)
        if i.isalpha():
            #print('isalpha')
            if not buffer:
                result.append(last_letter)
            else:
                result.append(last_letter * (int(''.join(buffer))))
            #print('result: ', result)
            last_letter = i
            buffer = []
        else:
            #print('isdigit')
            buffer.append(i)
            #print('digit_gather: ', digit_gather)
    if not buffer:
        result.append(last_letter)
    else:
        result.append(last_letter * (int(''.join(buffer))))
    #print('result: ', result)
    final = ''.join(result)
    return final

if __name__ == '__main__':
    import doctest
    doctest.testmod()
