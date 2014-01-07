#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
ret = n
for i in range(1, n):
    ret += i * (n - i)
print(ret)
