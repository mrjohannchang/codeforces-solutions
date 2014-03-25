#!/usr/bin/python
# -*- coding: utf-8 -*-

print('.{}'.format('.'.join(c for c in map(str.lower, raw_input()) if c not in 'aoyeui')))
