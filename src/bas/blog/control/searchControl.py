#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2017年5月1日

@author: ZhengbinChen
'''
from django.http import request
from django.http.response import HttpResponse
import json
from django.shortcuts import render


from blog.modal.bookModal import BookModal
import getAuthorBrief

def setSearchToHTML(request):
    searchMain = request.GET['search_text']
    print "search main contaion : "+searchMain
    book = BookModal()
    searchResultList = book.searchBookList(searchMain)
    return render(request,"search_result.html",{"searchResultList":json.dumps(searchResultList,encoding="utf-8")},locals())

def getBookMainInfo(request):
    bookId = request.GET["bookId"]
    print "book id is : " + bookId
    book = BookModal()
    bookMainInfo = book.getBookMainInfo(bookId)
    bookMainInfoJson = json.loads(bookMainInfo,encoding="utf-8")
    print bookMainInfoJson['title']
    publishingInfo = book.getPublishingListByBookName(bookMainInfoJson['title'])
    return render(request,"book_info.html",{"bookMainInfo":json.dumps(bookMainInfo,encoding="utf-8"),"publishingInfo":json.dumps(publishingInfo,encoding="utf-8")},locals())

def getRelevanceBook(request):
    book = BookModal()
    bookId = request.GET['bookId']
    relevanceBook = book.getBookMainInfo(bookId)
    return HttpResponse(json.dumps(relevanceBook),content_type="application/json")
    
def getAuthorInfo(request):
    book = BookModal()
    request.encoding = "utf-8"
    authorName = request.GET['authorName']
    authorName.encode("utf-8")
    authorInfo = book.getAuthorInfo(authorName)
    authorUrl = getAuthorBrief.getHtml("https://book.douban.com/subject_search?search_text='"+authorName+"'")
    authorBrief = "暂无作者介绍。"
    if authorUrl != None:
        print authorUrl
        authorBrief = getAuthorBrief.getAuthorBrief(authorUrl)
    return render(request,"author.html",{"authorName":authorName,"authorInfo":json.dumps(authorInfo,encoding="utf-8"),"authorBrief":authorBrief,"authorUrl":authorUrl,"count":authorInfo["authorPublishCount"],"sorce":authorInfo["authorDoubanSorce"],"tabs":authorInfo["tabCount"]},locals())
    
def getAuthorPublishList(request):
    book = BookModal()
    request.encoding = "utf-8"
    authorName = request.GET['authorName']
    authorName.encode("utf-8")
    authorPublishList = book.searchBookList(authorName)
    return HttpResponse(json.dumps(authorPublishList),content_type="application/json")
    
    


