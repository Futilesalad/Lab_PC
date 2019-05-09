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
arcpy.env.workspace = r"D:\partimeJob\数据\2.25\huafeng\output"
rasterlist = arcpy.ListRasters("*", "tif")

# for raster in rasterlist:
#     desc = arcpy.Describe(raster)
#     print (raster)
#     print("data type: ",desc.dataType)
#     print("bandCount: ",desc.bandCount)
#     print("compressionType: ",desc.compressionType)
#     print("format: ",desc.format)
#     print("meanCellHeight: ",desc.meanCellHeight)
#     print("meanCellWidth: ",desc.meanCellWidth)
#     print("pixelType: ",desc.pixelType)
#     print("srname: ",desc.spatialReference.name)
#     print("srname: ",desc.spatialReference.linearUnitName)

myraster = arcpy.Raster(r"15软件网络及计算机服务核密度clip.tif")
myraster.save(r"E:\Code\Py_projection\ArcgisLearning\data\output\raster\myraster_test.tif")