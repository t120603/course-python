"""
Created on Fri Apr 20 11:36:10 2018
an exercise from coursera course

@author: Philip_Wu
"""

import math

def isPrime(n):
    'check n is a prime or not, return True/False'
    if n == 2:
        return True
    k = int(math.sqrt(n)) + 1
    for i in range(3, k, 2):
        if n % i == 0:
            return False
    return True

def isMersenne(n):
    'mersenne number: M = 2**P-1, where M & P shoule be prime number'
    m = 2**n-1
    if isPrime(m) == True:
        return True
    return False

idx = 0
x = 2
while idx < 10:
    try:
        if isPrime(x) == True:
            ##print('{} is a prime'.format(x))
            if isMersenne(x) == True:
                idx += 1
                print('No.{} Mersenne prime is {} / {}'.format(idx, x, 2**x-1))
        x += 1
    except Exception as e:
        print(e)
print('bye bye')
