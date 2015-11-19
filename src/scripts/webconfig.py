'''
Created on 2015-11-18

@author: Winne
'''
class WebConfig(object):
    station_url='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8820'
    query_url='https://kyfw.12306.cn/otn/leftTicket/query'
    queryTicketPrice_url='https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice'
    headers={
#             'Accept':'*/*',
#             'Accept-Encoding':'gzip, deflate, sdch',
#             'Accept-Language':'zh-CN,zh;q=0.8',
#             'Cache-Control':'no-cache',
#             'Connection':'keep-alive',
#             'Host':'kyfw.12306.cn',
#             'If-Modified-Since':0,
#             'X-Requested-With':'XMLHttpRequest',
            'Referer':'https://kyfw.12306.cn/otn/lcxxcx/init',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36'
    }
    