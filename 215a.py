#!/usr/bin/python
# -*- coding: utf-8 -*-
n = int(raw_input())
pedal = map(int, raw_input().split())
m = int(raw_input())
rwheel = map(int, raw_input().split())
dp = []

for i in pedal:
    for j in rwheel:
        if j % i == 0:
            dp.append(j / i)

dp.sort()
dp.reverse()
print(str(dp.count(dp[0])))
