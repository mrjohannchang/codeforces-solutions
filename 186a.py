#!/usr/bin/python
# -*- coding: utf-8 -*-

f = lambda: map(ord,list(raw_input()))
genome_1, genome_2 = f(), f()

n = len(genome_1)
m = len(genome_2)
if n != m or n < 1 or m < 1:
    print "NO"
    exit()

d = []
for i in xrange(n):
    if genome_1[i] ^ genome_2[i] != 0:
        d.append(i)
    if len(d) > 2:
        break

if len(d) != 2:
    print "NO"
    exit()

genome_1[d[0]] ^= genome_1[d[1]]
genome_1[d[1]] ^= genome_1[d[0]]
genome_1[d[0]] ^= genome_1[d[1]]

if genome_1 == genome_2:
    print "YES"
else:
    print "NO"
