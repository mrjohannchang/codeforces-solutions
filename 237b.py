#!/usr/bin/env python
# -*- coding: utf-8 -*-
def main():
    n = input()
    c = map(int, raw_input().split())
    table = list()
    dic = dict()
    for i in xrange(n):
        table.append(map(int, raw_input().split()))
    for i in xrange(n):
        for j in xrange(c[i]):
            dic[table[i][j]] = (i, j)
    counter = 0
    step = list()
    end = False
    buf = 0
    for i in xrange(n):
        for j in xrange(c[i]):
            buf += 1
            if dic[buf] != (i, j):
                counter += 1
                (k, l) = dic[buf]
                keys = dic.viewkeys()
                values = dic.viewvalues()
                for ii, val in enumerate(values):
                    if val == (i ,j):
                        dic[ii+1] = dic[buf]
                        break
                dic[buf] = (i, j)
                step.append('{} {} {} {}'.format(i+1, j+1, k+1, l+1))
            if i == n - 1 and j == c[i] - 1:
                end = True
                break
        if end:
            break
    print counter
    for i in xrange(counter):
        print ''.join(step[i])
if __name__ == '__main__':
    main()
