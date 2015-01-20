# -*- coding: utf-8 -*-

s = list(input())
n = len(s)
candidates = [s + ['.']]
res = 'NA'

for i in range(n):
    candidates.append(s[:i] + ['.'] + s[i:])

for s in candidates:
    legal = True
    for i in range((n + 1) // 2):
        if s[i] == s[-i-1] or s[i] == '.' or s[-i-1] == '.':
            continue
        legal = False
    if legal:
        res = s

if res != 'NA':
    for i in range((n + 1) // 2):
        if res[i] == '.':
            res[i] = res[-i-1]
        elif res[-i-1] == '.':
            res[-i-1] = res[i]
    res = [s if s != '.' else 'a' for s in res]
    res = ''.join(res)

print(res)
