# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 10:03:42 2019

@author: Samuel Venegas
"""

def main():
        #variable definiton
        sum_total = 0
        product_total = 1
        while (sum_total < 50 or product_total < 150):
            num = float (input ("Enter a number: "))
            if (num % 2) ==0:
                #even
                sum_total += num
            else: #odd
                product_total *= num
        print ("The final sum is %i and the product is %i"%(sum_total, product_total))
main()
