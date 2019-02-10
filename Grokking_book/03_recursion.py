#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
example code from chapter 3 recursion. grokking book
"""
# base case and recursion case
def countdown(i):
    print (i)
    if i<=0:  # base case
        return
    else :    # recursion case
        countdown(i-1)
        
countdown(100)

# the call stack

def greet2(name):
    print("how are you, " + name + "?")
    
def bye():
    print ("OK bye !")
    
def greet(name):
    print ("hello, " + name + "!")
    greet2(name)
    print ("getting ready to say bye...")
    bye()
    
greet("Sam")

# the call stack with recursion
def fact(x):
    if x== 1:
        return 1
    else :
        return x * fact(x-1)

fact(3)
