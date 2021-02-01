def main(numbers):
    """
    Given a sequence of integers. Build a new sequence of the same length. Each element of a new
    sequence should be calculated as a multiplication of elements of the original sequence except
    the element with the same index.  Think about possible corner cases.
    >>> main([1, 5, 3])
    [15, 3, 5]
    >>> main([1, 2, 2, 5, 8])
    [160, 80, 80, 32, 20]
    """
    
    import numpy as np
    result = []
    num_tup = tuple(numbers)
    print(num_tup)
    for i in range(len(numbers)):
        print('i', i)
        a = list(numbers)
        print('a_pre-del', a)
        del a[i]
        print('a_post-del', a)
        product = np.prod(np.array(a))
        print('product', product)
        result.append(product)
        print ('result', result)
        print(' ')
        
    print (result)
    return result
main([1, 5, 3])
main([1, 2, 2, 5, 8])