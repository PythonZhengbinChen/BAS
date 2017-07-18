#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2017年4月30日

@author: ZhengbinChen
'''
from django.http import request
from blog.modal.bookModal import BookModal
from django.http.response import HttpResponse
import json

def getTopTenBookInfo(request):
        book = BookModal()
        topBookList = book.getTopTenBookInfo()
        print "get top ten book information!"
        return HttpResponse(json.dumps(topBookList),content_type="application/json")

def getTopTenAuthor(request):
        book = BookModal()
        topAuthor = book.getTopTenAuthor()
        print "get top ten auhtor information!"
        return HttpResponse(json.dumps(topAuthor),content_type="application/json")

def getTopTenPublishing(request):
        book = BookModal()
        topPublishingList = book.getTopTenPublishing()
        print "get top ten publishing information!"
        return HttpResponse(json.dumps(topPublishingList),content_type="application/json")