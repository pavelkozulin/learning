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

    return ' '.join(i[::-1] for i in text.split(' '))

reverse_words("Let's take LeetCode contest")
reverse_words('')
reverse_words(' ')
reverse_words('foo')
reverse_words(' bar ')
reverse_words('foo.bar')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
