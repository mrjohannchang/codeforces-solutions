#!/usr/bin/env python3


k, a, b, v = map(int, input().split(' '))
ans = 1
cur_section_count = 1

while a > 0:
    a -= v
    if a <= 0:
        break
    if cur_section_count < k and b > 0:
        cur_section_count += 1
        b -= 1
    else:
        cur_section_count = 1
        ans += 1

print(ans)
