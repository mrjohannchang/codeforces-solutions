#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
for a, b in zip(list(x for x in raw_input()), list(y for y in raw_input())):
    if a == b: print("0", end="")
    else: print("1", end="")
