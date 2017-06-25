# -*- coding: utf-8 -*-


def solve(a, n):
    for i in range(n):
        for j in range(n):
            v = a[i][j]
            if v == 1:
                continue
            s = [a[i][x] + a[y][j] for x in range(n) for y in range(n)]
            if v not in s:
                return False
    return True


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
print('Yes' if solve(a, n) else 'No')
