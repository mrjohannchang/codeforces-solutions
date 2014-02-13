#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def main():
    a, d =map(lambda x: int(float(x) * 10000 + 1e-6), input().split(' '))
    ans = []

    for i in range(1, int(input()) + 1):
        cur_round_pos = d * i % (a * 4)
        if cur_round_pos <= a:
            y = 0
            x = cur_round_pos / 10000
        elif cur_round_pos <= a * 2:
            x = a / 10000
            y = (cur_round_pos - a) / 10000
        elif cur_round_pos <= a * 3:
            y = a / 10000
            x = (a * 3 - cur_round_pos) / 10000
        elif cur_round_pos < a * 4:
            x = 0
            y = (a * 4 - cur_round_pos) / 10000
        ans.append('{} {}'.format(x, y))

    print('\n'.join(ans))

if __name__ == '__main__':
    sys.exit(main())
