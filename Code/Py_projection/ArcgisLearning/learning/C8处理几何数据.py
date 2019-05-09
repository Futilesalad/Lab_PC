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
from __future__ import print_function,unicode_literals,absolute_import

import fileinput

import arcpy


# arcpy.env.workspace = r"D:\partimeJob\数据\4.25\张鹏飞\仁怀数据\仁怀数据"
arcpy.env.workspace = r"E:\Code\Py_projection\ArcgisLearning\data\output"
arcpy.env.overwriteOutput = True
fc = "D:\partimeJob\本地数据\全国数据\国界.shp"
fc2 = r"D:\partimeJob\数据\4.25\张鹏飞\仁怀数据\仁怀数据\景点.shp"


# with arcpy.da.SearchCursor(fc,["OID@","SHAPE@"]) as cursor:
#     for row in cursor:
#         print("Feature {0}:".format(row[0]))
#         # for point in row[1].getPart(0):
#         partnum = 0
#         for part in row[1]:
#             print("Part {0}:".format(partnum))
#             for point in part:
#                 if point:
#                     print("{0}, {1}".format(point.X,point.Y))
#                 else:
#                     print("Interior Ring")
#             partnum += 1


infile = r"E:\Code\Py_projection\ArcgisLearning\data\points.txt"

fcnew = "new_polygon.shp"

# arcpy.CreateFeatureclass_management(r"E:\Code\Py_projection\ArcgisLearning\data\output",fcnew,"Polygon")
#
# cursor = arcpy.da.InsertCursor(fcnew,["SHAPE@"])
# array = arcpy.Array()
# point = arcpy.Point()
#
# for line in fileinput.input(infile):
#     point.ID, point.X, point.Y = line.split()
#     array.add(point)
# polygon = arcpy.Polygon(array)
# cursor.inserRow([polygon])
# fileinput.close()
# del cursor


coordlist = [[17.0, 20.0], [125.0,32.0],[4.0, 87.0]]
pointlist = []
for x, y in coordlist:
    point = arcpy.Point(x,y)
    pointgeometry = arcpy.PointGeometry(point)
    pointlist.append(pointgeometry)
arcpy.Buffer_analysis(pointlist,'buffer_test.shp', "10 METERS")
