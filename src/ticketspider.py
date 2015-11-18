#coding:utf-8  
'''
Created on 2015-11-18
爬取火车票信息
@author: Winne
'''
import sys
import urllib
import urllib2
from scripts.sqltool import DBmanager
from scripts.ticketinfo import TicketInfo
from scripts import webconfig, ticketinfo
WEBCONFIG=webconfig.WebConfig
class TicketSpider():
    
    def __init__(self):
        self.__query_url=WEBCONFIG.query_url
        self.__queryTicketPrice_url=WEBCONFIG.queryTicketPrice_url
    
    #获得站点信息
    def get_station_info(self):
        #从数据库读取站点code
        SQL_tool=DBmanager()
        SQL_tool.connectdb()
        station_codes=SQL_tool.searchtableinfo_byparams(['stationinfo'], ["code"])[0]
        SQL_tool.closedb()
        print station_codes[0]
        ticket_info=TicketInfo(tuple2str(station_codes[0]),tuple2str(station_codes[10]),'2015-11-25')
        req = urllib2.Request(
                              url=self.__query_url+'?'+ticket_info.head+'.train_date='+ticket_info.train_date+'&'+ticket_info.head+'.from_station='+ticket_info.from_station+'&'+ticket_info.head+'.to_station='+ticket_info.to_station+'&purpose_codes=ADULT'
        )
        data= urllib2.urlopen(req).read() #读出内容
        print data
    
    
    #获得列车价格
    
    #存入本地数据库
def tuple2str(s):
    return "".join(tuple(s))      
if __name__ == "__main__":   
    TicketSpider().get_station_info()
    
