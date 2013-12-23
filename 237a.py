#!/usr/bin/env python
# -*- coding: utf-8 -*-
def main():
    res, buf = 1, 1
    prev_h, prev_m = '0', '0'
    for _ in xrange(input()):
        h, m = raw_input().split()
        if h == prev_h and m == prev_m:
            buf += 1
            res = max(buf, res)
        else:
            buf = 1
            prev_h, prev_m = h, m
    print res
if __name__ == '__main__':
    main()
