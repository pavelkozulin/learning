import collections

def Most_frequent_element(array):
    '''
    Дан массив a из n целых чисел. Напишите программу, которая найдет число, которое чаще других встречается в массиве.
    Ограничение времени: 2 с, ограничение памяти: 256 МБ.

    Формат ввода
    В первой строке входных данных записано число n (1 ≤ n ≤ 300 000).
    Во второй строке записаны n целых чисел ai (0 ≤ ai ≤ 1 000 000 000).

    Формат вывода
    Выведите единственное число x, наибольшее из чисел, которое чаще других встречается в массиве a.

    >>> Most_frequent_element([1,1,2])
    1
    >>> Most_frequent_element([1,1,2,2])
    2
    >>> Most_frequent_element([2,2,1,1])
    2
    >>> Most_frequent_element([1,2,3])
    3
    >>> Most_frequent_element([1])
    [1]
    >>> Most_frequent_element([-1,1,-1])
    -1

    '''

    if len(array) == 1:
        return array
    element_frequency_dict = collections.Counter(array)

    max_count = 1
    max_element = 1

    for i in element_frequency_dict:
        if element_frequency_dict[i] > max_count:
            max_count = element_frequency_dict[i]
            max_element = i
        if element_frequency_dict[i] == max_count and max_element < i:
            max_element = i
    return max_element

if __name__ == '__main__':
    import doctest
    doctest.testmod()
