n, m = map(int, input().split())
original_name = input()
changes = [input().split() for _ in range(m)]

original_char_dict_list = sorted(list(set(original_name)))
modified_char_dict_list = sorted(list(set(original_name)))

for pair in changes:
    for i, c in enumerate(modified_char_dict_list):
        if c == pair[0]:
            modified_char_dict_list[i] = pair[1]
        elif c == pair[1]:
            modified_char_dict_list[i] = pair[0]

dictionary = {c: modified_char_dict_list[i] for i, c in enumerate(original_char_dict_list)}
name_list = list(original_name)

for i, c in enumerate(name_list):
    name_list[i] = dictionary[c]

print(''.join(name_list))
