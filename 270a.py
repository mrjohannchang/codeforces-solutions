#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for _ in range(int(input())):
    angle = int(input())
    if 60 <= angle < 180:
        if not 360 % (180 - angle):
            print('YES')
            continue
    print('NO')
