# -*- coding: utf-8 -*-

n = int(input())
l = map(int, input().split())
p, c = 0, 0

for i in l:
    if i > 0:
        p += i
    else:
        if p > 0:
            p -= 1
        else:
            c += 1

print(c)
