#!/usr/bin/python
# -*- coding: utf-8 -*-
teams = [raw_input() for i in xrange(input())]
win_times = reduce(max, [teams.count(i) for i in teams])
print([i for i in teams if win_times == teams.count(i)][0])
