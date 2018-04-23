# -*- coding: utf-8 -*-
"""
抽取豆瓣某本書的前50條短評內容並計算評分的平均值
Created on Mon Apr 23 09:01:02 2018

@author: Philip_Wu
"""

import requests, re, time
from bs4 import BeautifulSoup

count = 0
i = 0
score_s, count_s = 0, 0
while count < 50:
    try:
        r = requests.get('https://book.douban.com/subject/20429677/comments/hot?p='+str(i+1))
    except Exception as err:
        print(err)
        break
    soup = BeautifulSoup(r.text, 'lxml')
    comments = soup.find_all('p', 'comment-content')
    for item in comments:
        count = count+1
        print(count,'> ',item.string)
        if count == 50:
            break
    pattern = re.compile('<span class="user-stars allstar(.*?) rating"')
    p = re.findall(pattern, r.text)
    for star in p:
        count_s += 1
        score_s += int(star)
    time.sleep(5)   # delay request from douban's robuts.txt
    i += 1
    
if count == 50:
    print('average of user scores is '.format(score_s/count))
