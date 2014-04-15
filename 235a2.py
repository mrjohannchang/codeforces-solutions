# -*- coding: utf-8 -*-


n = int(input())
gcd = lambda a, b: b if a % b == 0 else gcd(b, a % b)

if n % 2:
    res = n * (n - 1) * (n - 2)
else:
    for i in range(n - 3, 0, -2):
        if gcd(n, i) != 1 or gcd(n - 1, i) != 1:
            continue
        res = max(n * (n - 1) * i,
                int(n * (n - 1) / 2) * (n - 2),
                (n - 1) * (n - 2) * (n - 3))
        break

if n < 3:
    res = n

print(res)
