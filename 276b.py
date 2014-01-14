#!/usr/bin/env python
# -*- coding: utf-8 -*-
s = raw_input()
r = sum(s.count(c) % 2 for c in set(s))
print 'First' if r == 0 or r & 1 == 1 else 'Second'
