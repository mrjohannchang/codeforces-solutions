# -*- coding: utf-8 -*-

a = [len(input()[2:]), 'A']
b = [len(input()[2:]), 'B']
c = [len(input()[2:]), 'C']
d = [len(input()[2:]), 'D']
ans = None

l = list(sorted([a, b, c, d]))

if l[0][0] * 2 <= l[1][0] and l[2][0] * 2 > l[3][0]:
    ans = l[0][1]
elif l[2][0] * 2 <= l[3][0] and l[0][0] * 2 > l[1][0]:
    ans = l[3][1]
else:
    ans = 'C'

print(ans)
