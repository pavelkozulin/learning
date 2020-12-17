def reverse_words(text):
    '''
    >>> reverse_words("Let's take LeetCode contest")
    "s'teL ekat edoCteeL tsetnoc"
    >>> reverse_words('')
    ''
    >>> reverse_words(' ')
    ' '
    >>> reverse_words('foo')
    'oof'
    >>> reverse_words(' bar ')
    ' rab '
    >>> reverse_words('foo  bar')
    'oof  rab'
    >>> reverse_words('foo.bar')
    'rab.oof'
    '''
    j, result = 0, []
    for i in range(len(text)):
        if text[i] == ' ':
            result.append(text[i - j: i][::-1])
            result.append(' ')
            j = 0
        elif i == len(text)-1:
            result.append(text[i - j: i + 1][::-1])
        else:
            j += 1
    myString = ''.join(result)
    return myString

reverse_words("Let's take LeetCode contest")
reverse_words('')
reverse_words(' ')
reverse_words('foo')
reverse_words(' bar ')
reverse_words('foo.bar')




if __name__ == '__main__':
    import doctest
    doctest.testmod()
