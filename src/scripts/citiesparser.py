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
        self.__station_buffer=self.__get_station_buffer()
        self.__station_buffer = self.__station_buffer.split("'")[1]
        unformatted_station=self.__station_buffer.split('@')
        station_list=[]
        for original_station in unformatted_station:
            if original_station and len(original_station) > 1:
                split_station = original_station.split('|')
                station_info = StationInfo(split_station[0], split_station[1], split_station[2], split_station[3],int(split_station[5]))
                station_list.append(station_info)
        return station_list

if __name__ == "__main__":   
     CitiesParser().parse_city()
     
