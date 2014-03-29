# -*- coding: utf-8 -*-

input()
a = list(map(int, input().split()))
s = [[], [], []]
for i in a:
    if i < 0:
        s[0] += [str(i)]
    elif i > 0:
        s[1] += [str(i)]
    else:
        s[2] += [str(i)]
if len(s[1]) == 0:
    s[1].extend(s[0][:2])
    s[0] = s[0][2:]
if len(s[0]) % 2 == 0:
    s[2].append(s[0][0])
    s[0] = s[0][1:]
for l in s:
    print(len(l), ' '.join(l))
