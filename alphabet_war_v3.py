def fight(text):
    """
    >>> fight('')
    "Let's fight again!"
    >>> fight('wqa')
    'Left side wins!'
    >>> fight('z')
    'Right side wins!'
    >>> fight('wma')
    "Let's fight again!"
    >>> fight('pma')
    'Right side wins!'
    >>> fight('wwwwwwz')
    'Left side wins!'
    >>> fight('y')
    'Left side wins!'
    >>> fight('aaaaaaaaaaasz')
    'Center wins!'
    """
    
    Left = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'y': 3}
    Right = {'m': 4, 'q': 3, 'd': 2, 'z': 1, 'y': 1}
    Center = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'y': 1}
    
    score = [sum([Left[i] for i in text if i in Left]),
             sum([Right[i] for i in text if i in Right]),
             sum([Center[i] for i in text if i in Center])
             ]
    
    if score.count(max(score)) > 1:
        result = "Let's fight again!"
    else:
        if score.index(max(score)) == 0:
            result = 'Left side wins!'
        if score.index(max(score)) == 1:
            result = 'Right side wins!'
        if score.index(max(score)) == 2:
            result = 'Center wins!'
   
    return result
    
fight('')
fight('wqa')
fight('z')
fight('wma')
fight('pma')
fight('wwwwwwz')
fight('y')
fight('aaaaaaaaaaasz')

if __name__ == '__main__':
    import doctest
    doctest.testmod()