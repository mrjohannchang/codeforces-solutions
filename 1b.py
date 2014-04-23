# -*- coding: utf-8 -*-


def is_rxcy(coordinate):
    if coordinate[0] == 'R' and coordinate[1] in '0123456789':
        if 'C' in coordinate:
            return True
    return False

def rxcy_to_excel(coordinate):
    SYMBOL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    row = coordinate[1:coordinate.rindex('C')]
    column = int(coordinate[coordinate.rindex('C')+1:])
    res = [row]

    while column > 0:
        column -= 1
        res = [SYMBOL[column % 26]] + res
        column = column // 26

    return ''.join(res)

def excel_to_rxcy(coordinate):
    SYMBOL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(coordinate)):
        if coordinate[i] not in SYMBOL:
            break
    row = coordinate[i:]
    column = coordinate[:i]
    res = 'R' + row + 'C'

    t = 0
    for c in column:
        t = t * 26 + SYMBOL.index(c) + 1
    res += str(t)

    return res

ans = []

for _ in range(int(input())):
    coordinate = input()
    if is_rxcy(coordinate):
        ans.append(rxcy_to_excel(coordinate))
    else:
        ans.append(excel_to_rxcy(coordinate))

print('\n'.join(ans))
