def most_sessions(sessions):
    '''
    Вам дана история сессий на некотором вымышленном сервисе. Каждая сессия характеризуется временем начала и временем окончания si и fi,
    для удобства все эти значения различны.
    Найдите такой момент времени t, когда было активно наибольшее количество сессий. Если таких моментов несколько,
    то выведите самый ранний из них. Ограничение времени: 1 с, ограничение памяти: 256 МБ.

    Формат ввода:
        В первой строке входных данных записано целое число n (1 ≤ n ≤ 1000).
        Далее в n строках записано через пробел по два целых числа si и fi (0 ≤ si < fi ≤ 1 000 000 000).

    >>> most_sessions([[0,5],[1,2],[2,3]])
    2
    >>> most_sessions([[0,5],[1,2]])
    1
    '''
    dict_all = {}
    for i in sessions:
        for k in range(i[0], i[1]+1):
            if k in dict_all:
                dict_all[k] += 1
            else:
                dict_all[k] = 1
    max_count = 1
    for j in dict_all:
        if dict_all[j] > max_count:
            max_count = dict_all[j]
            min_element = j
    return min_element

if __name__ == '__main__':
    import doctest
    doctest.testmod()
