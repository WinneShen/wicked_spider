# -*- coding: utf-8 -*-
'''
Created on 2015-11-18

@author: Winne
'''
class TicketInfo(object):
    head='leftTicketDTO'
    train_date=''
    from_station=''
    to_station=''
    purpose_codes='ADULT'
    
    def __init__(self,from_station='',to_station='',train_date=''):
        self.to_station=to_station
        self.from_station=from_station
        self.train_date=train_date
        
    def set_train_info(self,train_no='',station_train_code='',from_station_no='',to_station_no='',\
                       start_time='',arrive_time='',lishiValue=0,seat_types='',train_type=''):
        self.train_no=train_no
        self.station_train_code=station_train_code
        self.from_station_no=from_station_no
        self.to_station_no=to_station_no
        self.start_time=start_time
        self.arrive_time=arrive_time
        self.lishiValue=lishiValue
        self.train_type=train_type
        self.seat_types=seat_types
    
        
    def set_ticket_price(self,price_A9=None,price_P=None,price_M=None,price_O=None,price_A6=None,\
                         price_A4=None,price_A3=None,price_A2=None,price_A1=None,price_WZ=None):
        self.price_A9=price_A9
        self.price_P=price_P
        self.price_M=price_M
        self.price_O=price_O
        self.price_A6=price_A6
        self.price_A4=price_A4
        self.price_A3=price_A3
        self.price_A2=price_A2
        self.price_A1=price_A1
        self.price_WZ=price_WZ