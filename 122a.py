#!/usr/bin/env python
# -*- coding: utf-8 -*-
n = input()
print "YNEOS"[all([n%i for i in[4,7,47,74,444,447,474,477,744,747,774,777]])::2]
