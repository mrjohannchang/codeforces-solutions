#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
inputs = sys.stdin.read().split()
for v in inputs[1:]:
    if len(v) > 10:
        print('{}{}{}'.format(v[0], str(len(v)-2), v[len(v)-1]))
    else:
        print(v)
