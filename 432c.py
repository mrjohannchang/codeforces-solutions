# -*- coding: utf-8 -*-

import bisect


def gen_primes(upper_bound):
    upper_bound += 1
    t = [0] * (upper_bound)
    primes = [2]
    for i in range(3, upper_bound, 2):
        if t[i]:
            continue
        primes.append(i)
        for j in range(i + i, upper_bound, i):
            t[j] = 1
    return primes

def main():
    n = int(input())
    a = list(map(int, input().split()))
    primes = gen_primes(n + 1)
    process = list()
    d = [0] * n

    for i in range(n):
        d[a[i] - 1] = i

    i = 0
    while i < n:
        if a[i] == i + 1:
            i += 1
            continue
        r = d[i]
        l = r - primes[bisect.bisect(primes, r - i + 1) - 1] + 1
        a[l], a[r] = a[r], a[l]
        process.append('{} {}'.format(l + 1, r + 1))
        d[a[l] - 1] = l
        d[a[r] - 1] = r

    print(len(process))
    print('\n'.join(process))

if __name__ == '__main__':
    main()
