# -*- coding: utf-8 -*-


def main():
    n = int(input())
    teams = [input().split() for _ in range(n)]
    ans = [list((0, 0)) for _ in range(n)]
    home = dict()

    for i in range(n):
        home[teams[i][0]] = home.get(teams[i][0], 0) + 1

    for i in range(n):
        ans[i][0] = n - 1 + home.get(teams[i][1], 0)
        ans[i][1] = n - 1 - home.get(teams[i][1], 0)

    for i in range(n):
        ans[i] = '{} {}'.format(ans[i][0], ans[i][1])

    print('\n'.join(ans))

if __name__ == '__main__':
    main()
