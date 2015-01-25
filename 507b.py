# -*- coding: utf-8 -*-

import math

r, x, y, xp, yp = map(int, input().split())
print((math.ceil(math.sqrt((xp-x)*(xp-x) + (yp-y)*(yp-y))) + 2*r - 1) // (2 * r))
