import itertools


def sum_unique(string, table):
    for i in string:
        if table.find(i) == -1:
            table += i
    return table


def find(table, el, size_a, size_b):
    for i, j in itertools.product(range(size_a), range(size_b)):
        if table[i][j] == el:
            return i, j


def proverca(first, second, table):
    if first[0] == second[0]:
        return table[first[0]][(first[1] + 1) % len(table[0])] + table[second[0]][(second[1] + 1) % len(table[0])]
    elif first[1] == second[1]:
        return table[(first[0] + 1) % len(table)][first[1]] + table[(second[0] + 1) % len(table)][second[1]]
    else:
        return table[first[0]][second[1]] + table[second[0]][first[1]]
