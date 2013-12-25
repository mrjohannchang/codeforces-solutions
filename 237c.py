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
def main():
    res = -1
    primes = gen_primes(1000000)
    a, b, k = map(int, raw_input().split())
    buf = 0
    for l in xrange(1, b - a + 2):
        for x in xrange(a, b - l + 2):
            for i in xrange(x, x + l):
                if i in primes:
                    
    print res
if __name__ == '__main__':
    main()
