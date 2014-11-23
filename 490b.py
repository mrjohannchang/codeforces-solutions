# -*- coding: utf-8 -*-

import bisect

n = int(input())
pairs = [list(map(int, input().split())) for _ in range(n)]

front_set = set()
rear_set = set()

for pair in pairs:
    front_set.add(pair[0])
    rear_set.add(pair[1])

students = [-1] * n

pairs.sort()
fronts = [pair[0] for pair in pairs]
rears = [pair[1] for pair in pairs]

pos = 0
students[pos + 1] = rears[pos]
pos += 2

while pos + 1 < len(pairs):
    i = bisect.bisect_left(fronts, students[pos - 1])
    students[pos + 1] = rears[i]
    pos += 2

students[0] = [i for i in front_set - rear_set][0]
pos = 1
while pos + 1< len(pairs):
    i = bisect.bisect_left(fronts, students[pos - 1])
    students[pos + 1] = rears[i]
    pos += 2

print(' '.join(map(str, students)))
