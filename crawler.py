#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Crawler
Created on Sun Apr 22 11:02:05 2018

@author: jiakwan2
"""
import requests
from bs4 import BeautifulSoup
import re

sum = 0
r = requests.get('https://book.douban.com/subject/26727997/comments')
soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('p', 'comment-content')
for item in pattern:
    print(item.string)
pattern_s = re.compile('<span class="user-stars allstar(.*?) rating"')
p = re.findall(pattern_s, r.text)
for star in p:
    sum += int(star)
    
print('user star summary: {}'.format(sum))
