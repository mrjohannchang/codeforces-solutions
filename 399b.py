#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n, s = int(input()), input()
print(sum(2 ** i for i in range(n) if s[i] == 'B'))
