n, k = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(k)]
x = [0] * (n + 1)
y = [0] * (n + 1)
res = 0

for i, row in enumerate(m):
    for j, v in enumerate(row):
        if j == 0:
            continue
        x[v] = j
        y[v] = i

no = 1
for i, v in enumerate(m[y[1]]):
    if i < 2:
        continue
    if v != m[y[1]][i-1] + 1:
        no = i - 1
        break
    no = i

res += n - no

for i, row in enumerate(m):
    if i != y[1]:
        res += row[0] - 1
    else:
        res += row[0] - x[no]

print(res)
