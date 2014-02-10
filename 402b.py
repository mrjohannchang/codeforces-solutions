#!/usr/bin/env python3


n, k = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
upper_bound = 1
base_height = 1
ans = None

for i in range(len(a)):
    upper_bound = max(upper_bound, a[i] - k * i)

for i in range(1, upper_bound + 1):
    ans_candi = sum(1 for j in range(len(a)) if a[j] - i - k * j)
    if ans == None or ans_candi < ans:
        ans = ans_candi
        base_height = i

print(ans)
for i in range(len(a)):
    diff = a[i] - base_height - i * k
    if diff:
        print('{} {} {}'.format('-' if diff > 0 else '+', i + 1, abs(diff)))
