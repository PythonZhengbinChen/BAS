#!/usr/bin/python
#-*- coding: utf-8 -*-
'''
Created on 2017年4月30日

@author: ZhengbinChen
'''

import db
import json

class BookModal(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.DB = db.DBConn()
        self.conn = self.DB.getDBConn()
        self.collection = self.conn['bookInfo']
    '''
        首页获取热门书籍
    '''
    def getTopTenBookInfo(self):
        topBookCur = self.collection.find({"doubanScore": {"$gt": " 9.8 "}},{"_id":False}).sort([("doubanScore",-1)]).limit(10)
        topBookList = []
        for topBook in topBookCur:
            Information = {
                "title" : topBook["title"],
                "url" : topBook["url"],
                "coverpagePic" : topBook["coverpagePic"],
                "author" : topBook["author"],
                "publishing" : topBook["publishing"],
                "publishTime" : topBook["publishTime"]
            }
            topBookList.append(json.dumps(Information,encoding="utf-8"))
        topBookCur.close()
        self.DB.clossDBConn()
        return topBookList
    '''
        首页获取热门作者
    '''
    def getTopTenAuthor(self):
        topAuthorCur = self.collection.aggregate([
                {"$unwind": "$author"},
                {"$group": {"_id": "$author","Total":{"$sum":1}}},
                {"$sort" : {"Total":-1}},
                {"$limit": 10}
            ])
        topAuthorList = []
        for authorStr in topAuthorCur:
            author = {
                "_id": authorStr["_id"],
                "Total": authorStr["Total"]
                }
            topAuthorList.append(json.dumps(author,encoding="utf-8"))
        topAuthorCur.close()
        self.DB.clossDBConn()
        return topAuthorList
    '''
        首页获取热门出版社
    '''
    def getTopTenPublishing(self):
        topPublishingCur = self.collection.aggregate([
                {"$unwind": "$publishing"},
                {"$group": {"_id": "$publishing","Total":{"$sum":1}}},
                {"$sort" : {"Total":-1}},
                {"$limit": 11}
            ])
        topPublishingList = []
        for publishingStr in topPublishingCur:
            if publishingStr["_id"] == "null":
                continue
            publishing = {
                "_id": publishingStr["_id"],
                "Total": publishingStr["Total"]
                }
            topPublishingList.append(json.dumps(publishing,encoding="utf-8"))
        topPublishingCur.close()
        self.DB.clossDBConn()
        return topPublishingList
    
    '''
        根据用户条件searchMain查询书名、作者、出版社
    '''
    def searchBookList(self,searchMain):
        searchResultCur = self.collection.find({"$or":[{"title":searchMain},{"author":searchMain},{"publishing": searchMain}]},{"_id":False}).limit(20)
        searchResultList = []
        for searchResult in searchResultCur:
            searchResultList.append(json.dumps(searchResult,encoding="utf-8"))
        searchResultCur.close()
        self.DB.clossDBConn()
        return searchResultList
    '''
        获取bookId对应的书籍信息
    '''
    def getBookMainInfo(self,bookId):
        bookMainInfoCur = self.collection.find({"url":"https://book.douban.com/subject/"+bookId+"/"},{"_id":False}).limit(1)
        bookMainInfo = ""
        for bookMainInfoN in bookMainInfoCur:
            bookMainInfo = json.dumps(bookMainInfoN,encoding="utf-8")
            print bookMainInfo
        bookMainInfoCur.close()
        self.DB.clossDBConn()
        return bookMainInfo
    '''
        根据书籍名字获取出版社
    '''
    def getPublishingListByBookName(self,bookName):
        publishingCur = self.collection.aggregate([
                {"$match": {"title":bookName}},
                {"$unwind": "$publishing"},
                {"$group": {"_id": "$publishing"}}
            ])
        publishingList = []
        for publishingDuc in publishingCur:
            publishing = publishingDuc["_id"]
            print publishing
            publishTimeCur = self.collection.find({"title":bookName,"publishing":publishing},{"_id":False})
            for publishTime in publishTimeCur:
                publishingInfo = {
                    "publishing": publishing,
                    "publishTime": publishTime["publishTime"]
                    }
            publishingList.append(publishingInfo)
        publishTimeCur.close()
        publishingCur.close()
        self.DB.clossDBConn()
        return publishingList
    '''
        查收作者信息
    '''
    def getAuthorInfo(self,authorName):
        authorCurTab = self.collection.aggregate([
                {"$match": {"author":authorName}},
                {"$unwind": "$tab"},
                {"$group": {"_id": "$tab","Total":{"$sum":1}}},
                {"$sort": {"Total": -1}}
            ])
        authorTab = ""
        tabCount = 0
        for i,author in enumerate(authorCurTab):
            if i == 0:
                authorTab = author["_id"]
            tabCount += 1
        authorCurTab.close()
        authorPublishCountCur = self.collection.aggregate([
                {"$match": {"author":authorName}},
                {"$unwind": "$title"},
                {"$group": {"_id": "$title","Total":{"$sum":1}}},
                {"$sort": {"Total": -1}}
            ])
        authorPublishCount = 0
        for authorPublish in authorPublishCountCur:
            authorPublishCount += 1
        authorDoubanSorceCur = self.collection.aggregate([
                {"$match": {"author":authorName}},
                {"$unwind": "$author"},
                {"$group": {"_id": "$author","min":{"$min":"$doubanScore"},"max":{"$max":"$doubanScore"}}},
                {"$sort": {"Total": -1}},
                {"$limit": 1}
            ])
        authorDoubanSorce = 0
        for authorDouban in authorDoubanSorceCur:
            if authorDouban["min"].strip() == "":
                min = 8.5
            else:
                min = float(authorDouban["min"].strip())
                
            if authorDouban["max"].strip() == "":
                max = 9.5
            else:
                max = float(authorDouban["max"].strip())
            authorDoubanSorce = (min + max) / 2
        authorDoubanSorceCur.close()
        authorInfo = {
                "authorTab": authorTab,
                "tabCount": tabCount,
                "authorPublishCount": authorPublishCount,
                "authorDoubanSorce": authorDoubanSorce
            }
        self.DB.clossDBConn()
        return authorInfo
        
        