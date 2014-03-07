#!/usr/bin/python
# -*- coding: utf-8 -*-

players = raw_input()
if '0000000' in players or '1111111' in players:
    print('YES')
else:
    print('NO')
