#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt
a, b, c = map(int, raw_input().split())
x, y, z = sqrt(a * b / c), sqrt(a * c / b), sqrt(b * c / a)
print int(x * 4 + y * 4 + z * 4)
