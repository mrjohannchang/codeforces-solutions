#!/usr/bin/python
# -*- coding: utf-8 -*-

word = raw_input()
if len(word) > 1:
    if str.upper(word) == word:
        print(str.lower(word))
    elif str.upper(word[1:]) == word[1:]:
        print('{}{}'.format(str.upper(word[0]), str.lower(word[1:])))
    else:
        print(word)
else:
    print('{}'.format(str.swapcase(word)))
