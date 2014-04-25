# -*- coding: utf-8 -*-


n = int(input())
hamsters = list(input())
count = 0

for i in range(n):
    if hamsters.count('x') == n // 2:
        break
    if hamsters.count('x') > n // 2:
        if hamsters[i] == 'x':
            count += 1
            hamsters[i] = 'X'
    else:
        if hamsters[i] == 'X':
            count += 1
            hamsters[i] = 'x'

print(count)
print(''.join(hamsters))
