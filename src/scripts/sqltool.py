# -*- coding: utf-8 -*-
'''
Created on 2015-11-18

@author: Winne
'''
import sqlconfig
import MySQLdb
import time
class DBmanager:
    
    def __init__(self):
        sql_info=sqlconfig.SQLConfig()
        self.__host = sql_info.host
        self.__user=sql_info.username
        self.__passwd=sql_info.passwd
        self.__db=sql_info.database
        self.__port=sql_info.port
        self.__charset=sql_info.charset
        self.__connection_time=0
        self.__isconnect=False
        
    def connectdb(self):
        try:
            self.__conn=MySQLdb.connect(self.__host,self.__user,self.__passwd,self.__db,self.__port,charset=self.__charset)
            #print self.__host,self.__user,self.__passwd,self.__db,self.__port
            self.__cur=self.__conn.cursor()
            self.__isconnect=True       
            print "connet success"
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            if  self.__connection_time<3:
                print 'time out ! and reconnect'
                time.sleep(3)
                self.__connection_time=self.__connection_time+1
                self.connectdb()
            else:
                self.__isconnect=False
                print  'connect fail'
                
    def closedb(self):
        if  self.__isconnect:
            self.__cur.close()
            self.__conn.close()
            self.__isconnect=False
            print 'database has been closed'
        else:
            print 'has not connet'
            
    def inserttableinfo_byparams(self,table,select_params,insert_values):
        result=0
        if len(insert_values)<1 :
            print 'no insert values'
        elif  self.__isconnect:            
            try:
                sql='replace into '+table
                length=len(select_params)
                if length > 0:
                    sql+='('
                    for j in range(0,length-1):
                        sql=sql+select_params[j]+','
                    sql=sql+select_params[length-1]+')'
                    sql=sql+'    '
                    sql=sql+' values('    
                    for j in range(0,length-1):
                        sql=sql+'%s'+','    
                    sql=sql+'%s'+')'
                    result=self.__cur.executemany(sql,insert_values)
                    self.__conn.commit()
            except MySQLdb.Error,e:
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        else:
            print 'has not connet'
        return result
    
    def  searchtableinfo_byparams(self,table=[],select_params=[],request_params=[],equal_params=[]):
        if len(request_params)!=len(equal_params):
            print 'length of request_params,equals_params not match'
            return
        elif  self.__isconnect==True:
            try:
                sql='select     '
                length=len(select_params)
                if length > 0:
                    for j in range(0,length-1):
                        sql=sql+select_params[j]+','
                    sql=sql+select_params[length-1]
                else:
                    sql=sql+'*'
                sql=sql+' from '
                length=len(table)
                for j in range(0,length-1):
                    sql=sql+table[j]+','
                sql=sql+table[length-1]
                request_params_length=len(request_params)
                if request_params_length>0:
                    sql=sql+' where '
                    for k in range(0,request_params_length-1):
                        sql=sql+request_params[k]+' = '+equal_params[k]+' and '
                    sql=sql+request_params[request_params_length-1]+' = '+equal_params[request_params_length-1]+'  '
                print sql
                count=self.__cur.execute(sql)
                if count>0:
                    result=self.__cur.fetchall()
                    content=self.__cur.description
                    col= len(content)
                    print result,content,count,col
                    return result,content,count,col
                else:
                    print '没有相关信息'
                    return (0,0,0,0)
            except MySQLdb.Error,e:
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        else:
            print 'has not connet' 
