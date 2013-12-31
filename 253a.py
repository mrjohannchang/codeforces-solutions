#!/usr/bin/env python
# -*- coding: utf-8 -*-
with open('input.txt') as f:
    question = f.read()
n, m = map(int, question.split())
with open('output.txt', 'w') as f:
    if n > m:
        f.write('BG' * m + 'B' * (n - m))
    elif n < m:
        f.write('GB' * n + 'G' * (m - n))
    else:
        f.write('GB' * n)
