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
import arcpy

# 使用游标访问数据 InsertCursor(in_table,field_names)
# SearchCursor(in_table,field_names,{where_clause},{spatial_reference},{explore_to_point})
# UpdateCursor(in_table,field_names,{where_clause},{spatial_reference},{explore_to_point})
arcpy.env.workspace = r"D:\partimeJob\数据\4.25\张鹏飞\仁怀数据\仁怀数据"
fc = "D:\partimeJob\本地数据\全国数据\国界.shp"
fc2 = r"D:\partimeJob\数据\4.25\张鹏飞\仁怀数据\仁怀数据\景点.shp"

fieldList = arcpy.ListFields(fc2)
for field in fieldList:
    print(field.name)

cursor = arcpy.da.SearchCursor(fc2,['景区名称'])

for row in cursor:
    print("景区名称 = {0}".format(row[0]))


# 通过循环插入多行数据
# insertcursor = arcpy.da.InsertCursor(fc2,['景区名称'])
# x = 1
# while x <= 5:
#     insertcursor.insertRow(["new insert" + str(x)])
#     x += 1



#更新游标

updatecursor = arcpy.da.UpdateCursor(fc2,['坐标X','坐标Y'])
for row in updatecursor:
    if row[0]:
        continue
    row[0] = 23.444444
    row[1] = 117.777777
    updatecursor.updateRow(row)

#with 语句更保险

with arcpy.da.SearchCursor(fc2,["景区名称",'坐标X','坐标Y']) as cursor:
    for row in cursor:
        print("景区名称 = {0},x: {1},y: {2}".format(row[0],row[1],row[2]))


with arcpy.da.UpdateCursor(fc2,['坐标X','坐标Y']) as updatecursor:
    for row in updatecursor:
        if row[0] == 23.444444:
            updatecursor.deleteRow()
            print("删除成功")


# 如果没使用with语句的画需要 删除游标对象，释放锁
del row
del updatecursor

fieldname = "坐标X"

delimfield = arcpy.AddFieldDelimiters(fc2,fieldname) #避免字段分隔符产生的错误

with arcpy.da.SearchCursor(fc2,["景区名称",'坐标X','坐标Y'],delimfield + "< 50") as cursor:
    for row in cursor:
        print(row)


fieldname = arcpy.ValidateFieldName("New%^")
arcpy.AddField_management(fc2,fieldname,"TEXT","","",12)


unique_name = arcpy.CreateUniqueName('景点.shp')

fullname = arcpy.ParseTableName(fc2)
print(fullname)
namelist = fullname.split(", ")
databasename = namelist[0]
ownername = namelist[1]
fcname = namelist[2]
print(databasename)
print(ownername)
print(fcname)


with arcpy.da.SearchCursor(fc2,["SHAPE@XY"]) as cursor:
    for row in cursor:
        x, y = row[0]
        print("{0} ,{1}".format(x,y))


with arcpy.da.SearchCursor(fc,["OID@","SHAPE@"]) as cursor:
    for row in cursor:
        print("Feature {0}:".format(row[0]))
        # for point in row[1].getPart(0):
        partnum = 0
        for part in row[1]:
            print("Part {0}:".format(partnum))
            for point in part:
                if point:
                    print("{0}, {1}".format(point.X,point.Y))
                else:
                    print("Interior Ring")
            partnum += 1
