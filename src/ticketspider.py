# coding:utf-8  
'''
Created on 2015-11-18
爬取火车票信息
@author: Winne
'''
import sys
import urllib
import urllib2
import json
from scripts.sqltool import DBmanager
from scripts.ticketinfo import TicketInfo
from scripts import webconfig, ticketinfo
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
WEBCONFIG = webconfig.WebConfig
class TicketSpider():
    
    def __init__(self):
        self.__query_url = WEBCONFIG.query_url
        self.__queryTicketPrice_url = WEBCONFIG.queryTicketPrice_url
    
    # 获得站点信息
    def get_tickets_info(self):
        # 从数据库读取站点code
        ticket_infos = []
        SQL_tool = DBmanager()
        SQL_tool.connectdb()
        station_codes = SQL_tool.searchtableinfo_byparams(['stationinfo'], ["code"])[0]
        SQL_tool.closedb()
        for i in range(len(list(station_codes))):
            for j in range(len(list(station_codes))):
                ticket_info = TicketInfo(tuple2str(station_codes[i]), tuple2str(station_codes[j]), '2015-11-25')
                url=self.__query_url + '?' + \
                                      ticket_info.head + '.train_date=' + ticket_info.train_date + '&' + \
                                      ticket_info.head + '.from_station=' + ticket_info.from_station + '&' + \
                                      ticket_info.head + '.to_station=' + ticket_info.to_station + \
                                      '&purpose_codes=ADULT'
                print url
                req = urllib2.Request(url=url,headers=WEBCONFIG.headers)                
                resp = urllib2.urlopen(req) 
                print resp.read()       
                data = json.load(resp)  # 读出内容
                print data
                if data['httpstatus'] == 200:
                    if len(data['data']) > 0:
                        for a_ticket in data['data']:
                            if a_ticket['queryLeftNewDTO']['controlled_train_flag']=='0':
                                ticket_info.set_train_info(a_ticket['queryLeftNewDTO']['train_no'], \
                                                           a_ticket['queryLeftNewDTO']['station_train_code'], \
                                                           a_ticket['queryLeftNewDTO']['from_station_no'], \
                                                           a_ticket['queryLeftNewDTO']['to_station_no'], \
                                                           a_ticket['queryLeftNewDTO']['start_time'], \
                                                           a_ticket['queryLeftNewDTO']['arrive_time'], \
                                                           int(a_ticket['queryLeftNewDTO']['lishiValue']), \
                                                           a_ticket['queryLeftNewDTO']['seat_types'], \
                                                           a_ticket['queryLeftNewDTO']['station_train_code'][0])
                                price_dict = self.__get_ticket_price(ticket_info.train_no, ticket_info.from_station_no, \
                                                                   ticket_info.to_station_no, ticket_info.seat_types, ticket_info.train_date)
                                ticket_info.set_ticket_price(price_dict['price_A9'], price_dict['price_P'], price_dict['price_M'], price_dict['price_O'], price_dict['price_A6'], price_dict['price_A4'], price_dict['price_A3'], price_dict['price_A2'], price_dict['price_A1'], price_dict['price_WZ'])                            
                else:
                    print data['httpstatus']
                    exit(1)
                ticket_infos.append(ticket_info)
        print len(ticket_infos)
        return ticket_infos
    
    # 获得列车价格
    def __get_ticket_price(self, train_no, from_station_no, to_station_no, seat_types, train_date):
        print train_no, from_station_no, to_station_no, seat_types, train_date
        price_dict = {'price_A9':None, 'price_P':None, 'price_M':None, 'price_O':None, 'price_A6':None, \
                    'price_A4':None, 'price_A3':None, 'price_A2':None, 'price_A1':None, 'price_WZ':None}
        url=self.__queryTicketPrice_url + '?' + \
                            'train_no=' + train_no + '&' + \
                            'from_station_no=' + from_station_no + '&' + \
                            'to_station_no=' + to_station_no + '&' + \
                            'seat_types=' + seat_types + '&' + \
                            'train_date=' + train_date
        print url
        req = urllib2.Request(url=url,headers=WEBCONFIG.headers)                
        resp = urllib2.urlopen(req)    
        print resp.read()    
        data = json.load(resp)
        if data['httpstatus'] == 200:
            for key, value in data['data'].items():
                if key == 'A9':
                    price_dict['price_A9'] = self.__yuan2float(value)
                elif key == 'P':
                    price_dict['price_P'] = self.__yuan2float(value)
                elif key == 'M':
                    price_dict['price_M'] = self.__yuan2float(value)
                elif key == 'O':
                    price_dict['price_O'] = self.__yuan2float(value)
                elif key == 'A6':
                    price_dict['price_A6'] = self.__yuan2float(value)
                elif key == 'A4':
                    price_dict['price_A4'] = self.__yuan2float(value)
                elif key == 'A3':
                    price_dict['price_A3'] = self.__yuan2float(value)
                elif key == 'A2':
                    price_dict['price_A2'] = self.__yuan2float(value)
                elif key == 'A1':
                    price_dict['price_A1'] = self.__yuan2float(value)
                elif key == 'WZ':
                    price_dict['price_WZ'] = self.__yuan2float(value)
        else:
            print 'query price error:' + data['httpstatus']
        return price_dict
    
    def __yuan2float(self, s):
        temp=s.encode("utf-8").replace('¥','')
        return float(temp)
    # 存入本地数据库
    
def tuple2str(s):
    return "".join(tuple(s)) 
    
if __name__ == "__main__":   
    TicketSpider().get_tickets_info()
    
