#!/usr/bin/python
# -*- coding: utf-8 -*-
p = [raw_input() for i in xrange(3)]
count = lambda x: sum(p[x].count(c) for c in "aeiou")
print("YNEOS"[count(0)!=5 or count(1)!=7 or count(2)!=5::2])
