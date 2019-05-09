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
import mysql.connector


conn = mysql.connector.connect(user='root', password='cdq615812~', database='test' )
print('connect success...')

cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20)) ')
cursor.execute('insert into user (id, name) values (%s, %s)',['1','Alan'])
print(cursor.rowcount)
conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user where id = %s',('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()