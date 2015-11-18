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
