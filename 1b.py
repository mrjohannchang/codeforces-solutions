#!/usr/bin/env python
# -*- coding: utf-8 -*-
n = input()

for _ in xrange(n):
    s = raw_input()
    i = s.find('C')
    if s.find('C') > 1 and 

a = None
exrc = 'ABDEFGHIJKLMNOPQSTUVWXYZ'
az = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for _ in xrange(n):
    inp = raw_input()
    if len(inp) >= 4 and inp[0] == 'R' and inp[1] != 'C' \
            and inp.count('R') == 1 and inp.count('C') == 1 \
            and len(set(exrc) & set(inp)) == 0:
        r, c = int(inp[1:inp.index('C')]), int(inp[inp.index('C')+1:])
        i = 0
        while True:
            if 26 * (26**i) >= c:
                break
            i += 1
        buf = []
        for j in xrange(i, -1, -1):
            for k in xrange(1, 27):
                if k * 26**j > c:
                    buf.append(k-1)
                    c -= (k - 1) * 26**j
                    break
            if c == 0:
                break
        cv = []
        for i in buf:
            cv.append(az[i-1])
        print ''.join(cv) + str(r)
    else:
        for i in xrange(len(inp)):
            if inp[i] in '0123456789':
                break
        c, r = inp[:i], inp[i:]
        cv = 0
        c = c[-1::-1]
        for i in xrange(len(c)):
            cv += (ord(c[i]) - 64) * 26**i
        print 'R' + str(r) + 'C' + str(cv)
