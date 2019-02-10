#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 21:56:05 2019

chapter 4 problems
"""

# P4.1 summation of a list
def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])


my_list=[1, 6, 4, 8]

sum(my_list)

# 4.2 count the number of items in a list
def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


count(my_list)

# find the max number in a list
def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if  list[0] > sub_max else sub_max

max(my_list)
