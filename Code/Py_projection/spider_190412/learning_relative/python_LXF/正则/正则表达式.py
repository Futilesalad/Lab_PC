#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'F_tile_chen'
__mtime__ = ''
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

import re
s = 'ABC\\-001'

s2 = r'ABC\-001'

r1 = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(r1)

r2 = re.match(r'\d{3}\-\d{3,8}$', '010 12345')
print(r2)

test = '010 12345'
re_ = r'\d{3}\-\d{3,8}$'
if re.match(re_, test):
    print('ok')
else:
    print('failed')


# 切分字符串

print(re.split(r'\s+','a b   c'))
print(re.split(r'[\s+\,]+','a,; b,;;   c'))
print(re.split(r'[\s+\,\;]+','a,; b,;;   c'))


##分组功能
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0),m.group(1),m.group(2))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())


#贪婪匹配
print(re.match(r'^(\d+)(0*)$', '102300').groups())

#非贪婪匹配
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print( re_telephone.match('010-12345').groups())

def is_valid_email(addr):
    r = re.compile(r'^[\w+\.]+@\w+\.\w+$')
    if r.match(addr):
        return True
    else:
        return False


print(is_valid_email('someone@gmail.com'))
print(is_valid_email('bill.gates@microsoft.com'))
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')