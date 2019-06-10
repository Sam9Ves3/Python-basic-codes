# -*- coding: utf-8 -*-
"""
Created on Sun May 19 19:34:19 2019

@author: Samuel Venegas
"""

#Multiple numbers of 5 and 7 between 0 and 1000
def multiples():
    sum = 0
    counter = 0
    x= range(0,100)
    for x in range(0,1000):
        if (x%35==0):
            sum += x
            counter +=1
    print ("The number divisibles of 5 and 7 is: ", counter)
    print ("Their sum is: ", sum)
multiples()
            