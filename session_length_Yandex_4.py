max_sessions = [[i, 1000000000] for i in range (0, 1000)]

def most_sessions(sessions):
    '''
    Вам дана история сессий на некотором вымышленном сервисе. Каждая сессия характеризуется временем начала и временем окончания si и fi,
    для удобства все эти значения различны.
    Найдите такой момент времени t, когда было активно наибольшее количество сессий. Если таких моментов несколько,
    то выведите самый ранний из них. Ограничение времени: 1 с, ограничение памяти: 256 МБ.

    Формат ввода:
        В первой строке входных данных записано целое число n (1 ≤ n ≤ 1000).
        Далее в n строках записано через пробел по два целых числа si и fi (0 ≤ si < fi ≤ 1 000 000 000).

    >>> most_sessions([[2,4],[1,2],[2,4]])
    2
    >>> most_sessions([[0,5],[1,2]])
    1
    >>> most_sessions(max_sessions)
    999
    '''

    si_list = [(s, True) for s, f in sessions]
    fi_list = [(f, False) for s, f in sessions]
    full_list = sorted(si_list + fi_list)
    counter = 0
    final_counter = 0
    for t, b in full_list:
        if b:
            counter += 1
        else:
            counter -= 1
        if final_counter < counter:
            final_counter = counter
            time = t
    return time

if __name__ == '__main__':
    import doctest
    doctest.testmod()
