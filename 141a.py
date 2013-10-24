#!/usr/bin/python
# -*- coding: utf-8 -*-

men = raw_input() + raw_input()
mixed = raw_input()

if len(men) != len(mixed):
    print('NO')
    exit()
else:
    for c in men:
        if men.count(c) != mixed.count(c):
            print('NO')
            exit()
print('YES')
