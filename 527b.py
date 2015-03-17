# -*- coding: utf-8 -*-

import string

n, s, t = int(input()), input(), input()
x, i, j = 0, -1, -1
sc_dict = {c: set() for c in string.ascii_lowercase}
tc_dict = {c: set() for c in string.ascii_lowercase}
sti_dict, tsi_dict = dict(), dict()

for ci, sc, tc in zip(range(n), s, t):
    if sc == tc:
        continue
    sc_dict[sc].add(tc)
    tc_dict[tc].add(sc)
    sti_dict[sc + tc] = ci
    tsi_dict[tc + sc] = ci
    x += 1

for c in string.ascii_lowercase:
    cs = sc_dict[c] & tc_dict[c]
    if not cs:
        continue
    c2 = cs.pop()
    x -= 2
    i = sti_dict[c + c2] + 1
    j = tsi_dict[c + c2] + 1
    break
else:
    for c in string.ascii_lowercase:
        if not sc_dict[c] or not tc_dict[c]:
            continue
        x -= 1
        i = sti_dict[c + sc_dict[c].pop()] + 1
        j = tsi_dict[c + tc_dict[c].pop()] + 1
        break

print(x)
print(i, j)
