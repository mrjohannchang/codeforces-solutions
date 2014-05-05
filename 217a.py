# -*- coding: utf-8 -*-

import sys


def main():
    n = int(input())
    drifts = dict()
    for _ in range(n):
        i, j = map(int, input().split())
        drifts[i] = drifts.get(i, set()) | set([j])
    drifts = [drifts[k] for k in drifts]
    groups = []

    i = 0
    group = set()
    while i < len(drifts):
        if not group:
            group |= drifts[i]
        j = i + 1
        modified = False
        while j < len(drifts):
            if group & drifts[j]:
                group |= drifts.pop(j)
                modified = True
                break
            j += 1
        if not modified:
            i += 1
            groups.append(group)
            group = set()

    print(len(groups) - 1)

if __name__ == '__main__':
    sys.exit(main())
