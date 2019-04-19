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
import math
import requests,time,os,urllib,json,csv
from pymongo import MongoClient
import coord_translater as CT
client = MongoClient("mongodb://localhost:27017/")
db = client['GaoDe']
# db.authenticate("user", "password")
col = db['gaode_poi'] # 连接集合

key = "706baa52917ebec24033159098a4841c"
part_n = 4

# left_bottom = CT.bd09_to_wgs84(112.968588,22.520978);  # 设置区域左下角坐标（百度坐标系）广州
# left_bottom = CT.bd09_to_wgs84(111.901681,27.853899);  # 设置区域左下角坐标（百度坐标系）长沙
left_bottom = [112.607507,27.974821]  # 设置区域左下角坐标（百度坐标系）长沙
# right_top = CT.bd09_to_wgs84(114.070063,23.940013); # 设置区域右上角坐标（百度坐标系）广州
# right_top = CT.bd09_to_wgs84(114.266566,28.667582); # 设置区域右上角坐标（百度坐标系）长沙
right_top = [113.109372,28.561557]; # 设置区域右上角坐标（百度坐标系）长沙

left_top = [left_bottom[0],right_top[1]]
right_bottom = [right_top[0],left_bottom[1]]


poi_types_all = ["010000","020000","030000","040000","050000","060000","070000","080000"
                 "090000","100000","110000","120000","130000","140000","150000","160000","170000","180000","190000","200000"
                 ,"220000","970000","990000"]
type_str = "|".join(poi_types_all)
keywords = []
keywords_str = "|".join(keywords)
Gaode_base_url = "https://restapi.amap.com/v3/place/polygon?polygon={0},{1}|{2},{3}&output=json&offset=25&types="+type_str+"&key="+key
target_region = '长沙市'

output_csv = open("E:\Code\Py_projection\spider_190412\Gaode\output"+"\\"+"Gaode_POI_CS_center.csv","w",encoding='utf-8',newline='')
f = csv.writer(output_csv)
f.writerow(['poi_name','poi_addr','lon','lat','type_L','type_M','type_S','pname','cityname','adname'])
def saveToMongo(json_data,collection):
    try:
        # a = collection.find(json_data)
        if collection.count_documents(json_data) == 0:
            collection.insert_one(json_data)
    except:
        print("保存过程中发生错误...")

def get_poi_details(jsondata):
    in_target_region = True
    n = 0
    data = jsondata['pois']
    data_count = len(data)
    for da in data:
        cityname = da['cityname']
        # print(cityname)
        if cityname != target_region:
            n+=1
            continue
        poi_name = da["name"]
        type = da['type']
        typelist = type.split(";")
        type_L = typelist[0]
        type_M = typelist[1]
        type_S = typelist[2]
        poi_addr = da['address']
        location = da['location']
        coord = location.split(",")
        coord_trans = CT.gcj02_to_wgs84(float(coord[0]),float(coord[1]))
        pname = da["pname"]

        adname = da['adname']
        f.writerow([poi_name,poi_addr,coord_trans[0],coord_trans[1],type_L,type_M,type_S,pname,cityname,adname])
        saveToMongo(da,col)
    if n == data_count:
        in_target_region = False
    return in_target_region

def url_Request(url):
    n = 0
    res = ''
    def makesure():
        try:
            res = json.loads(requests.get(url).text)
        except :
            return False
        return res
    r = makesure()
    while not r:
        time.sleep(0.5)
        print("重新请求......")
        n+=1
        if n > 120:
            print("发生错误...")
            break
    return r

def get_All_POIs(LT,RB,N=5,level=1):

    if type(LT) != list or len(LT) != 2:
        print("左上角输入坐标有误")
        return
    if type(RB) != list or len(RB) != 2:
        print("右下角角输入坐标有误")
        return
    print('*'*((level-1)*2)+"所在层级" + str(level) +"....")
    part_number = 1
    gap_x = math.fabs(RB[0] - LT[0])
    gap_y = math.fabs(RB[1] - LT[1])
    x_item = gap_x / N
    y_item = gap_y / N
    for i in range(N):
        for j in range(N):
            print(' ' * ((level - 1) * 2) + "已处理第" + str(level) + "层级 第" + str(part_number) + " 切片...")
            part_number += 1
            LT_coord = [LT[0]+i*x_item,LT[1]-j*y_item]
            RB_coord = [LT_coord[0]+x_item,LT_coord[1]-y_item]
            total_url = Gaode_base_url.format(LT_coord[0],LT_coord[1],RB_coord[0],RB_coord[1])

            response = url_Request(total_url)
            if not response:
                continue
            count = int(response['count'])
            # if count < 25:
            #     get_poi_details(response)


            if not get_poi_details(response):
                continue

            if count < 800 and count > 0:
                pages_num = math.ceil(count / 25)
                for i in range(pages_num):
                    page_url = total_url + "&pages=" + str(i + 1)
                    jsondata = url_Request(page_url)
                    if not jsondata:
                        continue
                    if type(jsondata) != dict:
                        print(jsondata)
                        continue
                    get_poi_details(jsondata)
            else:
                level += 1
                if level <= 18:
                    get_All_POIs(LT_coord, RB_coord, N=4, level=level)
            print(' ' * ((level - 1) * 2) + "已处理第" + str(level) + "层级 第" + str(part_number) + " 切片...")
            part_number += 1


if __name__ == "__main__":
    get_All_POIs(left_top,right_bottom)
    output_csv.close()
