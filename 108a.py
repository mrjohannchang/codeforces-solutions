#!/usr/bin/python
# -*- coding: utf-8 -*-
h, m = raw_input().split(":")
if int(h) < 6 or (int(h) > 9 and int(h) < 16) or (int(h) > 19 and int(h) < 23):
    if len(str(int(h))) > 1:
        if int("".join(reversed(h))) > int(m):
            print h + ":" + "".join(reversed(h))
        else:
            if int(h) + 1 == 16:
                print "20:02"
            else:
                print str(int(h) + 1) + ":" + "".join(reversed(str(int(h) + 1)))
    else:
        if int(h) * 10 > int(m):
            print h + ":" + str(int(h) * 10)
        else:
            if int(h) + 1 == 6:
                print "10:01"
            else:
                print "0" + str(int(h) + 1) + ":" + str(int(h) + 1) + "0"
elif int(h) > 5 and int(h) < 10:
    print "10:01"
elif int(h) > 15 and int(h) < 20:
    print "20:02"
else:
    if 32 > int(m):
        print "23:32"
    else:
        print "00:00"
