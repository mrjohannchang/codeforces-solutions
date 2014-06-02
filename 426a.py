# -*- coding: utf-8 -*-

n, s = map(int, input().split())
a = map(int, input().split())
print('NO' if sum(sorted(a)[:-1]) > s else 'YES')
