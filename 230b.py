# -*- coding: utf-8 -*-


def gen_primes(upper_bound):
    upper_bound += 1
    t = [0] * (upper_bound)
    primes = [2]
    for i in range(3, upper_bound, 2):
        if t[i]: continue
        primes.append(i)
        for j in range(i + i, upper_bound, i): t[j] = 1
    return primes

def main():
    tprimes = set([p * p for p in gen_primes(int(1E6))])
    _ = input()
    x = list(map(int, input().split()))
    print('\n'.join('YES' if i in tprimes else 'NO' for i in x))

if __name__ == '__main__':
    main()
