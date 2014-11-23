# -*- coding: utf-8 -*-

n = int(input())
students = list(map(int, input().split()))

subjects = [list() for i in range(3)]

for i in range(len(students)):
    subjects[students[i] - 1].append(i + 1)

if not all(subjects):
    print(0)
else:
    print(min(len(s) for s in subjects))
    for i in range(min(len(s) for s in subjects)):
        for j in range(3):
            print(subjects[j][i], end=' ')
        print()
