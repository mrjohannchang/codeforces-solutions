#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
l = map(str.split, [raw_input() for i in xrange(input())])
f = lambda *c: [v[0] for v in l for w in c if w == v[1]]
p = lambda s: print("\n".join(s))
if len(f("rat")) > 0: p(f("rat"))
if len(f("woman", "child")) > 0: p(f("woman", "child"))
if len(f("man")) > 0: p(f("man"))
if len(f("captain")) > 0: p(f("captain"))
