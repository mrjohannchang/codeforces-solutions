# -*- coding: utf-8 -*-
#!/usr/bin/env python3

n, x = map(int, input().split(' '))
lines = [input() for _ in range(n)]
distressed = 0
for line in lines:
    operator, operand = line.split(' ')
    operand = int(operand)
    distressed += 1 if operator == '-' and x < operand else 0
    x += operand if operator == '+' else 0 if x < operand else -operand
print(x, distressed)
