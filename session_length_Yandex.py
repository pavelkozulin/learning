import collections

def most_sessions(sessions):
    '''
    Вам дана история сессий на некотором вымышленном сервисе. Каждая сессия характеризуется временем начала и временем окончания si и fi,
    для удобства все эти значения различны.
    Найдите такой момент времени t, когда было активно наибольшее количество сессий. Если таких моментов несколько,
    то выведите самый ранний из них. Ограничение времени: 1 с, ограничение памяти: 256 МБ.

    Формат ввода:
        В первой строке входных данных записано целое число n (1 ≤ n ≤ 1000).
        Далее в n строках записано через пробел по два целых числа si и fi (0 ≤ si < fi ≤ 1 000 000 000).

    >>> most_sessions([[0,10],[3,6],[5,8]])
    5
    '''

    finale = []
    for i in sessions:
        temp = [finale.append(k) for k in range(i[0], i[1]+1)]
    element_frequency_dict = collections.Counter(finale)
    max_count = 1
    min_element = 0
    for i in element_frequency_dict:
        if element_frequency_dict[i] > max_count:
            max_count = element_frequency_dict[i]
            min_element = i
    return min_element

most_sessions([[0,10],[3,6],[5,8]])
