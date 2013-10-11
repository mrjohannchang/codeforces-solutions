#!/usr/bin/python
# -*- coding: utf-8 -*-

s = raw_input()
four_times = 0
seven_time = 0
for c in s:
    if c == "4":
        four_times += 1
    elif c == "7":
        seven_time += 1
if four_times > seven_time or (four_times != 0 and four_times == seven_time):
    print("4")
elif four_times < seven_time:
    print("7")
else:
    print("-1")
