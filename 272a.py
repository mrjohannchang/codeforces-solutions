#!/usr/bin/env python
# -*- coding: utf-8 -*-
n = input() + 1
finger = sum(map(int, raw_input().split()))
print sum(1 for i in xrange(finger + 1, finger + 6) if i % n != 1)
