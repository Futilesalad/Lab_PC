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

import os

print(os.name) #操作系统类型

print(os.environ) # 环境变量

print(os.environ.get("PATH"))


 #  查看当前的绝对路径
abspath =  os.path.abspath('.')
print(abspath)
#在某个目录下创建一个新目录
newpath = os.path.join(abspath,'testdir')

#创建新目录
os.mkdir(newpath)


# 删除新目录
os.rmdir(newpath)

filepath = "E:\Code\Py_projection\spider_190412\learning_relative\python_LXF\Dict2.py"

#拆分路径

splitpath = os.path.split(filepath)
print(splitpath)

print(os.path.splitext(filepath))


with open('test.txt','w') as f:
    f.write('Im created for test\n')

# 重命名
os.rename('test.txt','test_rename.txt')

# 删除文件

os.remove('test_rename.txt')

listdir = [x for x in os.listdir(".") if os.path.isdir(x)]

pylist = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

print("目录：",listdir)
print("文件 py： ",pylist)


##practice##

def search_file(path, text):
    return_dic = {}
    for file in os.listdir(path):
        currentpath = os.path.join(path,file)
        if os.path.isdir(currentpath):
            search_file(currentpath,text)
        else:
            if file.find(text) > -1 :
                return_dic[file] = currentpath
    return return_dic

dic = search_file(r"E:\Code\Py_projection\spider_190412\learning_relative\python_LXF",'ict')
for i, j in dic.items():
    print("文件：{0}，路径:{1}".format(i,j))