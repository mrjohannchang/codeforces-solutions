#!/usr/bin/python
# -*- coding: utf-8 -*-

a, b, c = map(int, raw_input().split())
print a * b + b * c + a * c - a - b - c + 1
