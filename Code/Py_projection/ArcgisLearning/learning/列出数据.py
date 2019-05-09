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

arcpy.env.workspace = "D:\partimeJob\本地数据\全国数据"
fclist = arcpy.ListFeatureClasses()  #返回要素类
rasterlist = arcpy.ListRasters('','tif')   # 返回栅格

fieldlist= arcpy.ListFields('省界_region.shp','','Interger')


print(fclist,"\n",rasterlist,"\n",fieldlist)
for field in fieldlist:
    print(field.name + " " + str(field.length))
    print("{0} is a type of {1} with a length of {2}".format(field.name,field.type,field.length))