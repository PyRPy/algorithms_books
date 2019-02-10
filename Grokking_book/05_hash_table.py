#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 14:06:33 2019

chapter 5 hash tables
"""

# example on page-78
book =  dict()
book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49

print (book)

print (book['avocado'])

# example on page-80
phone_book = {}
phone_book["jenney"] = 8675309
phone_book['emergency'] = 911

print(phone_book['jenney'])

# example on page-82
voted = {}

def check_voter(name):
    if voted.get(name):
        print('kick them out')
    else:
        voted[name] = True
        print('let them vote')


check_voter('tom')
check_voter('tom')

print(voted)
