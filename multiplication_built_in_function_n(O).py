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
    print('numbers', numbers)
    product  = 1
    for x in numbers:
        product = product * x 
    print('product', product)
    result = [int(product / i) for i in numbers]
    print('result', result)
    return result
main([1, 5, 3])
main([1, 2, 2, 5, 8])