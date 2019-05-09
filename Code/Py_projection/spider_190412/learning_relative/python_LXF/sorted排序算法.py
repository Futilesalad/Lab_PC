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

#Python内置的sorted()函数就可以对list进行排序：
print(sorted([36,5,-12,-6,4]))

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序

print(sorted([36,5,-12,-6,4], key=abs))

# 字符串
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))



# ===   ===

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(l):
    def sort_by_name(tup):
        return tup[0].lower()
    return sorted(l,key=sort_by_name)

def by_score(l):
    return sorted(l,key=lambda tup:tup[-1])
print(by_name(L))
print(by_score(L))
