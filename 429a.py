# -*- coding: utf-8 -*-

import sys


def dfs(tree, root, priv_root, cur_lvl, priv_lvl, diff, pick_list):
    if not tree:
        return
    stack = [(root, priv_root, cur_lvl, priv_lvl)]
    while stack:
        (root, priv_root, cur_lvl, priv_lvl) = stack.pop()
        if cur_lvl ^ diff[root]:
            cur_lvl ^= 1
            pick_list.append(str(root))
        stack += [(vertex, root, priv_lvl, cur_lvl)
                for vertex in tree[root] if vertex != priv_root]

def main():
    n = int(input())
    tree = dict()
    for _ in range(n - 1):
        (u, v) = map(int, input().split())
        tree[u] = tree.get(u, set()) | set([v])
        tree[v] = tree.get(v, set()) | set([u])
    init = [0] + list(map(int, input().split()))
    goal = [0] + list(map(int, input().split()))
    diff = [i ^ j for (i, j) in zip(init, goal)]
    pick_list = list()

    dfs(tree, 1, 0, 0, 0, diff, pick_list)

    num = len(pick_list)
    print(num)
    if num:
        print('\n'.join(pick_list))

if __name__ == '__main__':
    sys.exit(main())
