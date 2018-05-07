#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 15:04:19 2018

@author: jiakwan2
"""

def newusers():
    enter a name
    if the name is used in the system:
        enter again
    else:
        set the password
… …

def oldusers():
    Enter the  username and password
    if password is right:  
        print(name, 'welcome back ')  
    else:  
        print('login incorrect') 
    … …

def login():
    option = '''
             (N)ew User Login 
             (O)ld User Login
             (E)xit
                    '''
    Enter the option
    … …

if __name__ == '__main__':  
    login() 

