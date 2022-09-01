def UnTrisemus(shifr, key_word, size_a = 4, size_b = 8): # «ЩЕУЦНЙЖГ СЖКЙЕЖ», "работа"
    shifr = shifr.lower()                                # Вывод: ПРИЛЕТАЮ ЗАВТРА
    table_alfabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    shifr_table = ''
    shifr_table = sum(key_word, shifr_table)
    shifr_table = sum(table_alfabet, shifr_table)
    table = [[0] * size_b for i in range(size_a)]
    counter = 0
    message = ''
    for i in range(0,size_a):
        for j in range(0, size_b):
            table[i][j] = shifr_table[counter % 32]
            counter += 1
    for i in shifr:
        if i not in table_alfabet:
            message += i
        else:
            first = find(table, i,size_a,size_b)
            message += table[(first[0] - 1)][first[1]]
    return message, table


def sum(string, table):
    for i in string:
        if table.find(i) == -1:
            table += i
    return table


def find(table, el, size_a, size_b):
    for i in range(0, size_a):
        for j in range(0, size_b):
            if table[i][j] == el:
                return [i, j]
