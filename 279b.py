#!/usr/bin/env python
# -*- coding: utf-8 -*-
def main():
    get_input = lambda: map(int, raw_input().split())
    n, t = get_input()
    a = get_input()
    if n == 1 and a[0] <= t:
        print 1
        exit()
    res = 0
    buf = 0
    for i in xrange(n):
        if buf + a[i] > t:
            break
        buf += a[i]
        res += 1

    for i in xrange(0, n):
        if i + res >= n:
            break
        buf = buf - a[i] + a[i+res]
        while True:
            if i + res + 1 >= n:
                break
            if buf + a[i+res+1] > t:
                break
            buf += a[i+res+1]
            res += 1
    print res

if __name__ == '__main__':
    main()
