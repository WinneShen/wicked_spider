# -*- coding: utf-8 -*-
'''
Created on 2015-11-18
解析站点
@author: Winne
'''
import webconfig
import urllib2
import json
from stationinfo import StationInfo
from sqltool import DBmanager
WEBCONFIG = webconfig.WebConfig
class CitiesParser():
    
    def __init__(self):
        self.__station_url = WEBCONFIG.station_url
        
    #从服务端获取站点和站点代码对应关系
    def __get_station_buffer(self):
        response = urllib2.urlopen(self.__station_url)
        station_page = response.read()
        response.close()
        return station_page

    #解析站点和站点代码关系
    def __parse_city(self):
        station_buffer=self.__get_station_buffer()
        station_buffer = station_buffer.split("'")[1]
        unformatted_station=station_buffer.split('@')
        station_list=[]
        for original_station in unformatted_station:
            if original_station and len(original_station) > 1:
                split_station = original_station.split('|')
                station_info = StationInfo(split_station[0], split_station[1], split_station[2], split_station[3],int(split_station[5]))
                station_list.append(station_info)
        return station_list
    
    #存入本地数据库中
    def save_station_table(self):
        station_list=self.__parse_city()
        insert_values=[]
        for s in station_list:
            insert_values.append((s.id,s.code,s.name,s.quanpin,s.abbreviate))
        SQL_tool=DBmanager()
        SQL_tool.connectdb()
        result=SQL_tool.inserttableinfo_byparams('stationinfo', ["id","code","name","quanpin","abbreviate"], insert_values)
        SQL_tool.closedb()
        print result 

if __name__ == "__main__":   
     CitiesParser().save_station_table()
     
