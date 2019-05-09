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
import arcpy
arcpy.env.workspace = r'E:\Code\Py_projection\ArcgisLearning\data'
# arcpy.ImportToolbox('E:/Code/ArcGIS_module_export/My_toolbox.tbx','mytools') # 第二个参数是别名

tools = arcpy.ListTools("*_analysis")
# for tool in tools:
#     print arcpy.Usage(tool)
# arcpy.Exists('') #确定数据集存在与否
print arcpy.ListEnvironments()
# print arcpy.GetMessage() #获取运行消息
print arcpy.ProductInfo()