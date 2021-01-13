def fight(text):
    """
    >>> fight('')
    "Let's fight again!"
    >>> fight('abracadabra')
    'Left side wins!'
    >>> fight('z')
    'Right side wins!'
    >>> fight('zdqmwpbs')
    "Let's fight again!"
    >>> fight('zzzzs')
    'Right side wins!'
    >>> fight('wwwwwwz')
    'Left side wins!'
    >>> fight('y')
    'Left side wins!'
    """
    
    war_dict = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'm': -4, 'q': -3, 'd': -2, 'z': -1, 'y': 2}
    b = sum([war_dict[y]
        for y in text
        if y in war_dict
        ])
    if b > 0:
        result = 'Left side wins!'
    elif b < 0:
        result = 'Right side wins!'
    else:
        result = "Let's fight again!"
    return result
fight('')
fight('abracadabra')
fight('z')
fight('zdqmwpbs')
fight('zzzzs')
fight('wwwwwwz')
fight('y')

if __name__ == '__main__':
    import doctest
    doctest.testmod()