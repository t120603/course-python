# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 13:53:13 2018

@author: Philip_Wu
"""

score = eval(input("Enter the score: "))
if 0 <= score <= 100:
    if score >= 90:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "D"
    print("The grade of {} is {}".format(score, grade))
else:
    print("Invalid score")

while True:
    try:
        count = int(input('Enter cuont: '))
        price = float(input('Enter price for each one: '))
        pay = count * price
        print('The price is :', pay)
        break
    except ValueError:
        print('Error> Please enter numeric one. ')
