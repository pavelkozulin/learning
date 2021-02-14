def Most_ferquent_element(array):
    '''
    Дан массив a из n целых чисел. Напишите программу, которая найдет число, которое чаще других встречается в массиве.
    Ограничение времени: 2 с, ограничение памяти: 256 МБ.

    Формат ввода
    В первой строке входных данных записано число n (1 ≤ n ≤ 300 000).
    Во второй строке записаны n целых чисел ai (0 ≤ ai ≤ 1 000 000 000).

    Формат вывода
    Выведите единственное число x, наибольшее из чисел, которое чаще других встречается в массиве a.

    >>> Most_ferquent_element((1,1,2))
    1
    >>> Most_ferquent_element((1,1,2,2))
    2
    >>> Most_ferquent_element((2,2,1,1))
    2
    >>> Most_ferquent_element((1,2,3))
    3

    '''

    D_to_F = {}
    for i in array:
        if i not in D_to_F:
            D_to_F[i] = 1
        else: D_to_F[i] += 1
    max_count = 1
    max_digit = 1
    for i in D_to_F:
        if D_to_F[i] > max_count:
            max_count = D_to_F[i]
            max_digit = i
        if D_to_F[i] == max_count and max_digit < i:
            max_digit = i
    return max_digit

if __name__ == '__main__':
    import doctest
    doctest.testmod()
