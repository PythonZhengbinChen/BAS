#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2017年5月1日

@author: ZhengbinChen
'''

import re
import socket
import time
import urllib

from pyquery import PyQuery as pq

#获取页面源码并转换,获取作者页的url
#url = https://book.douban.com/subject_search?search_text='陈忠实'
def getHtml(url):
    try:
        print url
        socket.setdefaulttimeout(15)
        urlConnect = urllib.urlopen(url.encode("utf-8"))
        html = urlConnect.read()
        #将html源码转为目录树结构
        pqhtml = pq(html)
    except Exception,e:
        print str(e)
    finally:
        urlConnect.close()
    authorUrl = pqhtml(".result-item .content h3").find("a")
    return authorUrl.attr("href")

def getAuthorBrief(authorUrl):
    try:
        socket.setdefaulttimeout(15)
        urlConnect = urllib.urlopen(authorUrl)
        html = urlConnect.read()
        #将html源码转为目录树结构
        pqhtml = pq(html)
    except Exception,e:
        print str(e)
    finally:
        urlConnect.close()
    authorBrief = pqhtml(".bd .hidden").html()
    if authorBrief == None:
        authorBrief = pqhtml("#intro .bd").html()
    return authorBrief

#authorUrl = getHtml("https://book.douban.com/subject_search?search_text='陈忠实'")
#print getAuthorBrief(authorUrl)