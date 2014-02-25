#!/usr/bin/python
# -*- coding: utf-8 -*-
n = input()
if n <= 127:
    print 'byte'
elif n <= 32767:
    print 'short'
elif n <= 2147483647:
    print 'int'
elif n <= 9223372036854775807:
    print 'long'
else:
    print 'BigInteger'
