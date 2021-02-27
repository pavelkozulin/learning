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

    result = ''
    last_letter = ''
    digit_gather = ''

    for i in text:
        #print('i = ', i)
        if i.isalpha():
            #print('isalpha')
            if digit_gather == '':
                result += last_letter
            else:
                result += last_letter * int(digit_gather)
            #print('result: ', result)
            last_letter = i
            digit_gather = ''
        else:
            #print('isdigit')
            digit_gather += i
            #print('digit_gather: ', digit_gather)
    if digit_gather == '':
        result += last_letter
    else:
        result += last_letter * int(digit_gather)
    #print('result: ', result)
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
