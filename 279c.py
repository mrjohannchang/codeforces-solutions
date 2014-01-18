#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    get_input = lambda: map(int, raw_input().split())
    n, m = get_input()
    array = get_input()
    dales = [0] * n

    if n < 3:
        for _ in xrange(m):
            print 'Yes'
        exit()

    for i in xrange(1, n - 1):
        if array[i-1] > array[i] and array[i+1] > array[i]:
            dales[i] = 1

    for _ in xrange(m):
        l, r = get_input()
        if r - l <= 1:
            print 'Yes'
            continue
        printed = False
        for e in dales[l:r-1]:
            if e != 1:
                continue
            print 'No'
            printed = True
            break
        if printed:
            continue
        print 'Yes'

if __name__ == '__main__':
    main()
