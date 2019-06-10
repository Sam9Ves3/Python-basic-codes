# -*- coding: utf-8 -*-
"""
Created on Mon May 20 09:39:02 2019

@author: Samuel Venegas
"""

def multiples():
    sum = 0
    counter = 0
    x= range(0,100)
    for x in range(0,1000):
        if (x%7==0 and x%5==0):
            sum += x
            counter +=1
    print ("The mean of all the multiples of 7 and 5 between 0 and 1000 is", sum/counter)
multiples()