# -*- coding: utf-8 -*-


n = int(input())
questions = []

for _ in range(n):
    questions.append(input())

lower_bound, upper_bound = None, None

for q in questions:
    bound = int(q.split()[1])
    if (q.startswith('>') and q.endswith('Y')) or (q.startswith('<') and q.endswith('N')):
        if ('Y' in q and '=' not in q) or ('N' in q and '=' in q):
            bound += 1
        lower_bound = bound if lower_bound == None else max(bound, lower_bound)
    else:
        if ('Y' in q and '=' not in q) or ('N' in q and '=' in q):
            bound -= 1
        upper_bound = bound if upper_bound == None else min(bound, upper_bound)

if lower_bound != None and upper_bound != None and lower_bound > upper_bound:
    print('Impossible')
else:
    print(lower_bound if lower_bound != None else upper_bound)
