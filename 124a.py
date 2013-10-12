#!/usr/bin/env python
# -*- coding: utf-8 -*-
n, a, b = map(int, raw_input().split())
print n - max(a + 1, n - b) + 1
