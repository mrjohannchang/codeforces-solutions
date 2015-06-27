n = int(input())
a = list(map(int, input().split()))
z = [i for i in range(n)]
t = a[0] - 0

for i, v in enumerate(a):
    v += t if i % 2 else -t
    if v < 0:
        v += n
    elif v >= n:
        v -= n
    a[i] = v

print('Yes' if a == z else 'No')
