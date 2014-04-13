# -*- coding: utf-8 -*-

m, n = list(map(int, input().split()))
time_table = []

time_table.append([0] * n)
for _ in range(m):
    time_table.append(list(map(int, input().split())))

time_table = list(list(t) for t in zip(*time_table))
time_table.insert(0, [0] * (m + 1))

for i in range(1, len(time_table)):
    for j in range(1, len(time_table[i])):
        time_table[i][j] = max(time_table[i-1][j], time_table[i][j-1]) + time_table[i][j]

print(' '.join(str(i) for i in time_table[n][1:]))
