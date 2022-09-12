def UnPlafer(shifr, key_word, size_a = 4, size_b = 8): # «ПРИЛЕТАЮ ЗАВТРА», "работа"
    shifr = shifr.replace(' ', '').lower()             # вывод «НАЙМЙРГЩ ЖБГВАБ»
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
    for i in range(0, len(shifr), 2):
        first = find(table, shifr[i],size_a,size_b)
        second = find(table, shifr[i + 1], size_a, size_b)
        message += proverca(first,second,table)
    return message


def proverca(first, second, table):
    if first[0] == second[0]:
        return table[first[0]][first[1] - 1] + table[second[0]][second[1] - 1]
    elif first[1] == second[1]:
        return table[first[0] - 1][first[1]] + table[second[0] - 1][second[1]]
    else:
        return table[first[0]][second[1]] + table[second[0]][first[1]]


def sum(string, table):
    for i in string:
        if table.find(i) == -1:
            table += i
    return table


def find(table, el, size_a, size_b):
    for i in range(0, size_a):
        for j in range(0, size_b):
            if table[i][j] == el:
                return [i,j]

