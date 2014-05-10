# -*- coding: utf-8 -*-


n = int(input())
b = [list(input()) for _ in range(n)]

for i in range(1, n - 1):
    for j in range(1, n - 1):
        if b[i][j] == b[i-1][j] == b[i+1][j] == b[i][j-1] == b[i][j+1] == '#':
            b[i][j] = b[i-1][j] = b[i+1][j] = b[i][j-1] = b[i][j+1] = '.'
print('NO' if any(True for r in b if '#' in r) else 'YES')
