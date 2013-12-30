#!/usr/bin/env python
# -*- coding: utf-8 -*-
n = input()
print n if sum(map(int, raw_input().split())) % n == 0 else n - 1
