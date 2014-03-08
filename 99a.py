#!/usr/bin/python
# -*- coding: utf-8 -*-
s = raw_input()
ind = lambda x=0: s.index(".") + x
if int(s[ind(-1)]) == 9:
    print("GOTO Vasilisa.")
else:
    if len(s[:ind()]) > 1:
        print("{}{}".format(s[:ind(-1)], str(int(s[ind(-1)]) + int(int(s[ind(1)])>4))))
    else:
        print(str(int(round(float(s)))))
