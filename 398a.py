#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    a, b = map(int, input().split(' '))
    answer = -b ** 2
    a_cluster = a

    if a:
        for i in range(a):
            answer_candicate = (a - i) ** 2 + i

            quotient = b // (i + 2)
            remainder = b % (i + 2)

            answer_candicate -= ((i + 2) - remainder) * quotient ** 2 \
                    + remainder * (quotient + 1) ** 2

            if answer_candicate > answer:
                answer = answer_candicate
                a_cluster = a - i

    print(answer)
    if a:
        quotient = b // (a - a_cluster + 2)
        remainder = b % (a - a_cluster + 2)
        print('x' * quotient, end='')
        print('o' * a_cluster, end='')
        print('x' * (quotient + (1 if remainder else 0)), end='')
        remainder = max(remainder - 1, 0)
        for i in range(a - a_cluster):
            print('o', end='')
            print('x' * (quotient + (1 if remainder else 0)), end='')
            remainder = max(remainder - 1, 0)
        print()
    else:
        print('x' * b)

if __name__ == '__main__':
    main()
