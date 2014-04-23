# -*- coding: utf-8 -*-


white_list = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y']
name = input()
is_wrong = False

if len(set(white_list)) != len(set(white_list) | set(name)):
    is_wrong = True
else:
    for i in range(len(name) // 2):
        if name[i] != name[-(i+1)]:
            is_wrong = True
            break

print('NO' if is_wrong else 'YES')
