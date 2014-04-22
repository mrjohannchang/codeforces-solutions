# -*- coding: utf-8 -*-


n = int(input())
s = list(input())
count = 0
l, r = -1, 0
while True:
    if l == -1:
        if 'R' in s:
            r = s.index('R')
            if 'L' in s[:r]:
                l = s.index('L')
                count += r - l - 1
            else:
                count += r
            l = r
        elif 'L' in s:
            count = n - s.index('L') - 1
            break
        else:
            count = n
            break
    else:
        if s[l] == 'R':
            if 'L' in s[l:]:
                r += s[l:].index('L')
                if (r - l - 1) & 1:
                    count += 1
                l = r
            else:
                break
        else:
            if 'R' in s[l:]:
                r += s[l:].index('R')
                count += r - l - 1
                l = r
            else:
                count += n - l -1
                break

print(count)
