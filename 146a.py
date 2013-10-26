#!/usr/bin/env python
# -*- coding: utf-8 -*-
n = input()
ticket = map(int, list(raw_input()))
if set(ticket) != set([4, 7]) or sum(ticket[:n/2]) != sum(ticket[n/2:]):
    print 'NO'
    exit()
print 'YES'
