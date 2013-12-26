#!/usr/bin/env python
# -*- coding: utf-8 -*-
def main():
    y, k, n = map(int, raw_input().split())
    res = -1
    if y < n:
        res = list()
        for i in xrange(1, n - y + 1):
            if (i + y) % k == 0:
                res += [str(i)]
        if len(res) == 0:
            res = -1
    if res == -1:
        print res
    else:
        print ' '.join(res)
if __name__ == '__main__':
    main()
