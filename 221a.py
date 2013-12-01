#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = input()

if n == 1:
    print 1
    exit()
elif n == 2:
    print 2, 1
    exit()

l = []
for i in xrange(n):
    if i == 0:
        l.append(n)
        continue
    l.append(i)
print ' '.join(map(str, l))

# # test
# def f(l, x):
    # if x == 1:
        # return
    # f(l, x-1)
    # l[x-1], l[x-2] = l[x-2], l[x-1]

# # l = [1, 2, 3, 4, 5]
# l = [5, 1, 2, 3, 4]
# f(l, 5)
# print l
