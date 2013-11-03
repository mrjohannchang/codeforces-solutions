#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

cur_dir = '/'
for i in xrange(input()):
    cmd = re.sub('^\ *', '', raw_input())
    if cmd.startswith('pwd'):
        print(cur_dir)
        continue
    else:
        path = re.sub('^cd\ *', '', cmd)
        if path.startswith('/'):
            cur_dir = path
        else:
            cur_dir += path
        buf_list = []
        for j in cur_dir.split('/'):
            if j == '':
                continue
            if j == '..':
                size = len(buf_list)
                if size > 0:
                    del buf_list[size-1]
            else:
                buf_list.append(j)
        if len(buf_list) != 0:
            cur_dir = '/{}/'.format('/'.join(buf_list))
        else:
            cur_dir = '/'
        continue
