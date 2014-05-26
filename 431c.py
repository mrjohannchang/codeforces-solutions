# -*- coding: utf-8 -*-

(n, k, d) = map(int, input().split())

def get_ways(n, upper_bound):
    ways = [1] + [0] * n
    for i in range(1, n + 1):
        ways[i] = sum(ways[max(0, i - upper_bound):i])
    return ways[n]

print((get_ways(n, k) - get_ways(n, d - 1)) % (10 ** 9 + 7))
