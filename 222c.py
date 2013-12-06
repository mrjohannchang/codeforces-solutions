#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fractions import gcd
n, m = map(int, raw_input().split())
numerator = reduce(lambda x, y: x * y, map(int, raw_input().split()))
denumerator = reduce(lambda x, y: x * y, map(int, raw_input().split()))
divisor = gcd(numerator, denumerator)
print 1, 1
print str(numerator / divisor)
print str(denumerator / divisor)
