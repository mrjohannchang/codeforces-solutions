# -*- coding: utf-8 -*-

import datetime


c = input()
start_clock = datetime.datetime.strptime(c, '%H:%M')
end_clock = datetime.datetime.strptime(c, '%H:%M')

while end_clock.strftime('%H') != end_clock.strftime('%M')[::-1]:
    end_clock += datetime.timedelta(minutes=1)

print(int((end_clock-start_clock).total_seconds() // 60))
