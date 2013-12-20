#!/usr/bin/env python
# -*- coding: utf-8 -*-
def gen_primes(n):
    ret = [2]
    if n < 3:
        return ret
    n += 1
    buf = [0] * n
    buf[2] = 1
    for i in xrange(3, n, 2):
        if buf[i] == 0:
            ret.extend([i])
            for j in xrange(2 * i, n, i):
                buf[j] = 1
    return ret
def count_divisor(n, primes):
    ret = 1
    for p in primes:
        if n < p:
            break
        cnt = 1
        while n % p == 0:
            cnt += 1
            n /= p
        ret *= cnt
    return ret
def main():
    p = gen_primes(100)
    a, b, c = map(int, raw_input().split())
    a, b, c, ans = a + 1, b + 1, c + 1, 0
    buf = [1] * (a * b * c)
    for ai in xrange(1, a):
        for bi in xrange(1, b):
            for ci in xrange(1, c):
                i = ai * bi * ci
                if buf[i] == 1 and i > 1:
                    buf[i] = count_divisor(i, p)
                ans += buf[i]
    print ans
if __name__ == '__main__':
    main()
