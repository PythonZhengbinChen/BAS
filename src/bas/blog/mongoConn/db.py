#!/usr/bin/python
#-*- coding: utf-8 -*-
'''
Created on 2017年3月5日

@author: ZhengbinChen
'''
from pymongo import MongoClient
import pymongo


class DBConn(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
      
    def getDBConn(self):
        self.mongo = MongoClient("mongodb://localhost:27017")
        self.db = self.mongo['douban']
        return self.db
    
    def clossDBConn(self):
        self.mongo.close()
        print("Bye")