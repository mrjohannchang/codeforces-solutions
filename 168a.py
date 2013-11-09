#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import *
n, x, y = raw_input().split()
n, x, y = int(n), int(x), int(y)
puppet = 0
if x * 100 / n < y:
    puppet = int(ceil(n * float(y) / 100)) - x
print puppet
