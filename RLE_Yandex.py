def RLE(text):
    """
    Кодирование длин серий (RLE) — алгоритм сжатия данных, заменяющий повторяющиеся символы на один символ и число его повторов.
    Серией называется последовательность, состоящая из нескольких одинаковых символов (более одного).
    При кодировании строка одинаковых символов, составляющих серию, заменяется строкой, содержащей сам повторяющийся символ и
    количество его повторов.
    Например, строка AAAABBB будет сжата в строку A4B3, а строка AAAAAAAAAAAAAAABAAAAA — в строку A15BA5.
    Вам дана сжатая строка, найдите длину исходной строки. Длина исходной строки не превышает 1000 символов,
    все символы исходной строки — заглавные буквы латинского алфавита. Ограничение времени: 2 с, ограничение памяти: 264 МБ.
    Формат ввода:
    В единственной строке входных данных содержится непустая строка. Гарантируется, что эта строка является результатом
    корректного RLE-сжатия некоторой строки.
    Формат вывода:
    Выведите длину исходной строки.

    >>> RLE('A')
    1
    >>> RLE('A2')
    2
    >>> RLE('AB')
    2
    >>> RLE('A12B')
    13
    >>> RLE('AB12')
    13
    >>> RLE('A2B2C2')
    6
    """

    result, buffer = [], []
    for i in text:
        if i.isalpha():
            #print('case isalpha, i = ', i)
            if buffer != []:
                #print('subcase buffer != []')
                a = ''.join((map(str, buffer)))
                result.append(int(a))
                #result.append(-1)
                #result.append(1)
                buffer = []
                #print('result = ', result)
            else:
                #print('subcase buffer == []')
                result.append(1)
                #print('result = ', result)
        else:
            #print('case isdigit, i = ', i)
            buffer.append(int(i))
            #print('buffer = ', buffer)
    #print('buffer_exit_FOR = ', buffer)
    if buffer != []:
        a = ''.join((map(str, buffer)))
        result.append(int(a))
        result.append(-1)
    else:
        pass
    #print('result = ', result)
    #print(sum(result))
    return sum(result)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
