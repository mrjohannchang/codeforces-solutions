#!/usr/bin/env python
# -*- coding: utf-8 -*-

for i in range(int(input()) + 1, 10000):
    if len(set(list(str(i)))) == 4:
        print(i)
        break
