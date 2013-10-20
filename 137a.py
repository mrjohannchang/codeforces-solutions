#!/usr/bin/env python
# -*- coding: utf-8 -*-
s = raw_input()
carried_item = 1
time = 1
for i in xrange(1, len(s)):
    if s[i] == s[i-1] and carried_item < 5:
        carried_item += 1
    else:
        time += 1
        carried_item = 1
print time
