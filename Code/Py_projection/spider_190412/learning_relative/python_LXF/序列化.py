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
import pickle,json
d = dict(name='bob', age=20,score=88)
a1 = json.dumps(d)
print(a1)
a2  = '{"name": "bob", "age": 20, "score": 88}'
json_load = json.loads(a1)
print(json_load)

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
s = Student('bob',20,80)
def student2dic(std):
    return{'name':std.name,
           'age':std.age,
           'score':std.score}

class2json = json.dumps(s, default=student2dic)
print(json.dumps(s, default=student2dic))

print(json.dumps(s, default=lambda obj: obj.__dict__))

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

print(json.loads(class2json, object_hook=dict2student))


obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True) #
print(s)