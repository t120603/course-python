#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 15:37:32 2018

@author: jiakwan2
"""

from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests
import pymysql

# open database connection
conn = pymysql.connect('localhost', 'philip', 'wu45480480', 'GasPrice')
# use cursor() for 得到操作指標
mycur = conn.cursor()

def getData(url):
    try:
        html = requests.get(url).text
    except HTTPError as e:
        print(e)
        return None
    try:
        Obj = BeautifulSoup(html, 'html.parser')
        myList = []
        myData = Obj.find_all('span', attrs={'id':'Showtd'})
        myRows = myData[0].find_all('tr')
        for r in myRows:
            c = r.find_all('td')
            if (len(c[0].text) > 0 and len(c[1].text) > 0) and \
               (len(c[2].text) > 0 and len(c[3].text) > 0) and \
               (len(c[4].text) > 0):
                dataList = []
                dataList.append(c[0].text)
                dataList.append(c[1].text)
                dataList.append(c[2].text)
                dataList.append(c[3].text)
                dataList.append(c[4].text)
                myList.append(dataList)
    except AttributeError as e:
        return None
    return myList

mList = getData('https://new.cpc.com.tw/division/mb/oil-more4.aspx')
i= 0
for data in mList:
    if i < 5000:
        i += 1
        sqlstr = "insert into GasPrice values('{}', {}, {}, {}, {});".format( \
                    data[0], data[1], data[2], data[3], data[4])
        mycur.execute(sqlstr)
        conn.commit()
        
conn.close()
