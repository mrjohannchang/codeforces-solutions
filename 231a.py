#!/usr/bin/env python
# -*- coding: utf-8 -*-
print sum(1 for _ in xrange(input()) if raw_input().count('1') > 1)
