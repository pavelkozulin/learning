def most_sessions(sessions):
    '''
    Вам дана история сессий на некотором вымышленном сервисе. Каждая сессия характеризуется временем начала и временем окончания si и fi,
    для удобства все эти значения различны.
    Найдите такой момент времени t, когда было активно наибольшее количество сессий. Если таких моментов несколько,
    то выведите самый ранний из них. Ограничение времени: 1 с, ограничение памяти: 256 МБ.

    Формат ввода:
        В первой строке входных данных записано целое число n (1 ≤ n ≤ 1000).
        Далее в n строках записано через пробел по два целых числа si и fi (0 ≤ si < fi ≤ 1 000 000 000).

    >>> most_sessions([[0,5],[1,3],[2,3]])
    2
    >>> most_sessions([[0,5],[1,2]])
    1
    '''

    si_list, fi_list, full_list = [], [], []
    for i in sessions:
        si_list.append(i[0])
        fi_list.append(i[1])
    full_list = si_list + fi_list
    counter = 0
    final_counter = 0
    for j in range(min(full_list), max(full_list)):
        if j in si_list:
            counter += 1
        if j in fi_list:
            counter -= 1
        if final_counter < counter:
            final_counter = counter
            time = j
    return time

if __name__ == '__main__':
    import doctest
    doctest.testmod()
