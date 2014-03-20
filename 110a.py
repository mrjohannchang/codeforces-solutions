#!/usr/bin/python
# -*- coding: utf-8 -*-
number = raw_input()
total = number.count("4") + number.count("7")
if total is 4 or total is 7:
    print("YES")
else:
    print("NO")
