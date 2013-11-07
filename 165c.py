#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys

def main():
    k = int(input())
    s = '1' + input() + '1'
    indices = [i for i in range(len(s)) if s[i] == '1']
    ans = 0

    if k == 0:
        ans = sum((len(seg) + 1) * len(seg) // 2 for seg in s.split('1'))
    else:
        for i in range(k, len(indices) - 1):
            ans += (indices[i-k+1] - indices[i-k]) * (indices[i+1] - indices[i])

    print(ans)

if __name__ == '__main__':
    sys.exit(main())
