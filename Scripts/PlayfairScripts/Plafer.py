def Plafer(message, key_word, size_a = 4, size_b = 8): # «НАЙМЙРГЩ ЖБГВАБ», "работа"
    message = message.replace(' ', '').lower()        # Вывод ПРИЛЕТАЮ ЗАВТРА
    if len(message) % 2 == 1:
        message += "ъ"
    table_alfabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    shifr_table = ''
    shifr_table = sum(key_word, shifr_table)
    shifr_table = sum(table_alfabet, shifr_table)
    table = [[0] * size_b for i in range(size_a)]
    counter = 0
    shifr = ''
    for i in range(0,size_a):
        for j in range(0, size_b):
            table[i][j] = shifr_table[counter % 32]
            counter += 1
    for i in range(0, len(message), 2):
        first = find(table, message[i],size_a,size_b)
        second = find(table, message[i + 1], size_a, size_b)
        if first[0] == second[0] and first[1] == second[1]:
            third = find(table, "ъ", size_a, size_b)
            shifr += proverca(first,third, table)
            shifr += proverca(second,third, table)
        else:
            shifr += proverca(first,second,table)
    return shifr


def proverca(first, second, table):
    if first[0] == second[0]:
        return table[first[0]][(first[1] + 1) % len(table[0])] + table[second[0]][(second[1] + 1) % len(table[0])]
    elif first[1] == second[1]:
        return table[(first[0] + 1) % len(table)][first[1]] + table[(second[0] + 1) % len(table)][second[1]]
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
                return [i, j]
