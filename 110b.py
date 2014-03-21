#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
p = lambda x: print(x, end="")
for i in xrange(input()):
    if i % 4 == 0:
        p("a")
    elif i % 4 == 1:
        p("b")
    elif i % 4 == 2:
        p("c")
    else:
        p("d")
print()
