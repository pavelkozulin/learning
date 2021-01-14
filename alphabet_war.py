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
    
    Left = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'y': 3}
    Right = {'m': 4, 'q': 3, 'd': 2, 'z': 1, 'y': 1}
    Center = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'y': 1}
    
    if sum(Left.values()) > sum(Right.values()) and sum(Left.values()) > sum(Center.values()):
        result = 'Left side wins!'
    elif sum(Right.values()) > sum(Left.values()) and sum(Right.values()) > sum(Center.values()):
        result = 'Right side wins!'
    elif sum(Center.values()) > sum(Left.values()) and sum(Center.values()) > sum(Right.values()):
        result = 'Center side wins!'
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