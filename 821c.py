# -*- coding: utf-8 -*-


stack = []
next_pop_num = 1
r = 0


for _ in range(2 * int(input())):
    command = input()
    if command.startswith('add'):
        n = int(command[4:])
        stack.append(n)
    else:
        if stack and stack[-1] != next_pop_num:
            r += 1
            stack = []
        if stack:
            stack.pop(-1)
        next_pop_num += 1

print(r)
