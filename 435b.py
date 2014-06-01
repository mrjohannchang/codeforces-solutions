# -*- coding: utf-8 -*-

(a, k) = input().split()
a = list(a)
k = int(k)
sorted_a = list(reversed(sorted(a)))
i = 0

while k > 0 and a != sorted_a:
    for j in range(9, 0, -1):
        c = str(j)
        if c in a[i:] and a[i:].index(c) <= k:
            l = a[i:].index(c)
            k -= l
            a.insert(int(i), a.pop(i+l))
            break
    i += 1

print(''.join(a))
