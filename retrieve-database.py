#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 21:05:38 2018

@author: jiakwan2
"""

import pymysql
import matplotlib.pyplot as pt

db = pymysql.connect('localhost','philip','wu45480480','GasPrice')
mycur = db.cursor()

sqlstr = 'SELECT * FROM GasPrice'
try:
    listMonth = []
    listGas92 = []
    listGas95 = []
    listGas98 = []
    listGasW  = []
    xMonth = 1
    mycur.execute(sqlstr)
    # 使用fetchall()得到所有資料
    result = mycur.fetchall()
    for row in result:
        listMonth.append(xMonth)
        xMonth += 1
        listGas92.append(row[1])
        listGas95.append(row[2])
        listGas98.append(row[3])
        listGasW.append(row[4])
        print("%s, %6.2f, %6.2f, %6.2f, %6.2f" % (row[0],row[1],row[2], row[3], row[4]))
except:
    print("Error: unable to fetch data")
    
db.close()

pt.figure(num=None, figsize=(8,8), dpi=168, facecolor='w', edgecolor='k')
pt.plot(listMonth, listGas92, lw=2, label='Gas92')
pt.plot(listMonth, listGas95, lw=2, label='Gas95')
pt.plot(listMonth, listGas98, lw=2, label='Gas98')
pt.plot(listMonth, listGasW, lw=2, label='GasW')
pt.xlabel('month')
pt.ylabel('NT$')
pt.legend()
pt.title('Python Leraning')
pt.show()

