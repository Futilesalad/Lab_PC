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

from __future__ import print_function, unicode_literals, absolute_import
import arcpy

print(arcpy.Exists(r"D:\partimeJob\本地数据\全国数据\省界_region.shp"))
desc = arcpy.Describe(r"D:\partimeJob\本地数据\全国数据\省界_region.shp")
print("Data type: " + desc.shapeType)
print("File path: " + desc.path)
print("Catalog path: " + desc.catalogPath)
print("File name: "+ desc.file)
print("Base name: " + desc.baseName)
print("Name: " + desc.name)
sr = desc.spatialReference
print('Spatial reference: '+ sr.name)