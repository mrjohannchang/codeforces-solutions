#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

print(re.sub('^\ *|\ *$', '', re.sub('\ +', ' ', re.sub('WUB', ' ', raw_input()))))
