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
    
    Left_sum = sum([Left[i] for i in text if i in Left])
    Right_sum = sum([Right[i] for i in text if i in Right])
    Center_sum = sum([Center[i] for i in text if i in Center])
    
    score = [Left_sum, Right_sum, Center_sum]
    
    biggest = max(score)
    
    index = score.index(biggest)
    
    if score.count(biggest) > 1 :
        result = "Let's fight again!"
    else:
        if index == 0:
           result = 'Left side wins!'
        if index == 1:
            result = 'Right side wins!'
        if index == 2:
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