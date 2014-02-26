#!/usr/bin/python
# -*- coding: utf-8 -*-

class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = x, y, z
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

ff = Point(0, 0, 0)
for i in xrange(input()):
    x, y, z = map(int, raw_input().split())
    ff += Point(x, y, z)
if ff.x == 0 and ff.y == 0 and ff.z == 0:
    print("YES")
else:
    print("NO")
