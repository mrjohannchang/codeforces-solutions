#!/usr/bin/python
# -*- coding: utf-8 -*-

s1, s2 = list(raw_input()), list(raw_input())
for v in s2:
    if v == " ":
        continue
    if v in s1:
        s1.remove(v)
    else:
        print "NO"
        exit()
print "YES"
