def main(numbers):
    """
    See https://leetcode.com/problems/single-element-in-a-sorted-array/
    You are given a sorted array consisting of only integers where every element appears exactly
    twice, except for one element which appears exactly once. Find this single element that appears
    only once.
    Follow up: Your solution should run in O(log n) time and O(1) space.
    >>> main([1, 1, 2, 3, 3, 4, 4, 8, 8])
    2
    >>> main([3, 3, 7, 7, 10, 11, 11])
    10
    >>> main([])
    >>> main([1])
    1
    >>> main([1, 1, 2])
    2
    """
    
    if main ==[]:
        result = ''
    elif len(main) == 1:
        result = main[0]
    else:
        low = 0
        high = len(main) - 1
        mid = (high - low) // 2
        while True:
            if main[mid - 1] != main[mid] and main[mid] != main[mid + 1]:
                result = main[mid]
                print('xyz_mid')
                break
            elif high - low == 2:
                if main[mid - 1] == main[mid]:
                    result = main[mid + 1]
                if main[mid] == main[mid + 1]:
                    result = main[mid - 1]
                print('len = 3')
                break
            elif len(main) > 3:
                print('indexes', low, mid, high)
                print('values', main[low], main[mid], main[high])
                if (high - low) % 4 == 0:
                    print('%4=0') 
                    if main[mid] == main[mid + 1]:
                        low = mid
                    else:
                        high = mid
                elif (high - low) % 4 == 2:
                    print('%4=2') 
                    if main[mid] == main[mid - 1]:
                        low = mid + 1
                    else:
                        high = mid - 1
                mid = low + (high - low) // 2
    return relult