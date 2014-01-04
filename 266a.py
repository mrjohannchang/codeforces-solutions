#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
s = input()
print(sum(1 for i in range(0, n-1) if s[i] == s[i+1]))
