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
from functools import reduce


def f(x):
    return x**2

def red(x,y):
    return x*2+y
L = [1,2,3,4,5,6,7,8,9,10]

print(list(map(f,L)))
print(reduce(red,L))


DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,"6":6,'7':7,'8':8,'9':9}

def str2int(s):
    def char2num(s):
        return DIGITS[s]
    return reduce(lambda x,y: x * 10 + y,map(char2num,s))

a = str2int('234252')
print(a,type(a))

### practice #####

names = ['adam','LISA','barT']
def normalize(names):
    def f(n):
        return n.capitalize()
    return list(map(f,names))

print(normalize(names))

#接受一个列表利用reduce求积
def prod(L):
    def f(x,y):
        return x*y
    return reduce(f,L)
print(prod([3,5,7,9]))

#======== 字符串转浮点数 ==========
def str2float(s):
    if isinstance(s,str):
        l = s.split(".")
        pre = l[0]
        def d(s):
            return DIGITS[s]
        Pre = reduce(lambda x, y: x * 10 + y, map(d, pre))
        if s.rfind('.') == -1:
            return Pre
        last = l[-1]
        Last = reduce(lambda x,y:x*10+y, map(d,last))/(10**len(last))
        return Pre + Last
    raise TypeError('bad operand type')
print(str2float("123.456"))





# == fliter =====

def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,['A','','B',None,'C','  '])))



def _odd_iter():
    n = 1
    while True:
        n = n +2
        yield n

def _not_divisible(n):
    return lambda x:x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)


for n in primes():
    if n < 100:
        print(n)
    else:
        break


# === filter practice ===
# 筛选回数
def is_palindrome(n):
    # str_n = str(n)
    # s = ''
    # for i in range(len(str_n)):
    #     s+=str_n[-(i+1)]
    # return n == int(s)
    return str(n) == str(n)[::-1]


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')