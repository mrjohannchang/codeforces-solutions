#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = input()
print(s if int(s) >=0 else max(int(s), int(s[:-1]), int(s[:-2]+s[-1])))
