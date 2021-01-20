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
    
    low = 0 # индекс первого элемента
    
    high = len(main) - 1  # индекс последнего элемента
    
    mid = (low + high) // 2 # индекс серединного элемента
    
    
    while main[mid - 1] == main[mid] or main[mid] == main[mid + 1]:      # пока хотя бы пара из элеиентов с индексами mid-1, mid, mid+1 булут равны, то:
        if main[mid] == main[mid + 1] and len(main[mid: high]) % 2 == 0:  # если элеиенты с индексами mid+1 и mid равны И длина от mid до high есть четное число (то есть не содержит single element)
            high = mid                                                    # переписываем последний элемент как срединный
        if main[mid] == main[mid + 1] and len(main[mid: high]) % 2 == 1:  # если элеиенты с индексами mid+1 и mid равны И длина от mid до high есть НЕчетное число (то есть содержит single element)
            low = mid                                                     # переписываем первый элемент как срединный
        if main[mid] == main[mid - 1] and len(main[low: mid]) % 2 == 0:   # если элеиенты с индексами mid-1 и mid равны И длина от low до mid есть четное число (то есть не содержит single element)
            low = mid                                                     # переписываем первый элемент как срединный
        if main[mid] == main[mid - 1] and len(main[mid: high]) % 2 == 1:  # если элеиенты с индексами mid-1 и mid равны И длина от low до mid есть НЕчетное число (то есть содержит single element)
            high = mid                                                    # переписываем последний элемент как срединный
        mid = (low + high) // 2                                           # считаем новый индекс серединного элемента
    return main[mid] 