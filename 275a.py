#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    lights = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    for i in xrange(0, 3):
        r = map(int, raw_input().split())
        for j in xrange(0, 3):
            for k in xrange(0, 3):
                for l in xrange(0, 3):
                    if (k == 0 or k == 2) and (l == 0 or l == 2):
                        continue
                    lights[i+k][j+l] += r[j]

    for i in xrange(1, 4):
        for j in xrange(1, 4):
            lights[i][j] = 0 if lights[i][j] & 1 else 1

    for i in xrange(1, 4):
        print ''.join(map(str, lights[i][1:4]))

if __name__ == '__main__':
    main()
