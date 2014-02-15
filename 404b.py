#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def main():
    a, d =map(float, input().split(' '))
    ans = []

    for i in range(1, int(input()) + 1):
        cur_round_pos = d * i % (a * 4)
        if cur_round_pos <= a:
            y = 0
            x = cur_round_pos
        elif cur_round_pos <= a * 2:
            x = a
            y = (cur_round_pos - a)
        elif cur_round_pos <= a * 3:
            y = a
            x = (a - (cur_round_pos - a * 2))
        elif cur_round_pos < a * 4:
            x = 0
            y = (a - (cur_round_pos - a * 3))
        ans.append('{} {}'.format(x, y))

    print('\n'.join(ans))

if __name__ == '__main__':
    sys.exit(main())
